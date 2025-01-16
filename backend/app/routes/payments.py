from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
import stripe
from app.models.payment import Payment
from app.models.user import User
from app import db
from datetime import datetime
import os

payments_bp = Blueprint('payments', __name__)
stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

@payments_bp.route('/create-payment-intent', methods=['POST'])
@jwt_required()
def create_payment_intent():
    try:
        data = request.get_json()
        amount = data['amount']  # Amount in cents
        
        # Create payment intent with Stripe
        intent = stripe.PaymentIntent.create(
            amount=amount,
            currency='usd',
            metadata={'integration_check': 'accept_a_payment'}
        )
        
        return jsonify({
            'clientSecret': intent.client_secret
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@payments_bp.route('/submit-payment', methods=['POST'])
@jwt_required()
def submit_payment():
    try:
        user_id = get_jwt_identity()
        data = request.get_json()
        
        payment = Payment(
            user_id=user_id,
            amount=data['amount'],
            stripe_payment_id=data['stripe_payment_id'],
            status='completed',
            rent_for_month=datetime.strptime(data['rent_for_month'], '%Y-%m-%d').date()
        )
        
        db.session.add(payment)
        db.session.commit()
        
        return jsonify({'message': 'Payment recorded successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@payments_bp.route('/payment-history', methods=['GET'])
@jwt_required()
def payment_history():
    user_id = get_jwt_identity()
    payments = Payment.query.filter_by(user_id=user_id).order_by(Payment.payment_date.desc()).all()
    
    return jsonify([{
        'id': p.id,
        'amount': p.amount,
        'status': p.status,
        'payment_date': p.payment_date.isoformat(),
        'rent_for_month': p.rent_for_month.isoformat()
    } for p in payments]) 