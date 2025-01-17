from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from app.models.user import User
from app import db
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    try:
        logger.info('Received registration request')
        # Try to get JSON data first, then fall back to form data
        if request.is_json:
            data = request.get_json()
        else:
            data = request.form
            
        logger.info(f'Registration data received: {data}')
        
        # Check if user already exists
        if User.query.filter_by(email=data['email']).first():
            logger.warning(f'Email already registered: {data["email"]}')
            return jsonify({'error': 'Email already registered'}), 400
        
        # Create new user
        user = User(
            email=data['email'],
            password_hash=generate_password_hash(data['password']),
            first_name=data['first_name'],
            last_name=data['last_name'],
            apartment_number=data['apartment_number']
        )
        
        db.session.add(user)
        db.session.commit()
        
        logger.info(f'User registered successfully: {user.email}')
        return jsonify({'message': 'User registered successfully'}), 201
    except Exception as e:
        logger.error(f'Error during registration: {str(e)}')
        return jsonify({'error': str(e)}), 400

@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        logger.info('Received login request')
        # Try to get JSON data first, then fall back to form data
        if request.is_json:
            data = request.get_json()
        else:
            data = request.form
            
        logger.info(f'Login attempt for email: {data.get("email")}')
        user = User.query.filter_by(email=data['email']).first()
        
        if not user or not check_password_hash(user.password_hash, data['password']):
            logger.warning(f'Invalid login attempt for email: {data.get("email")}')
            return jsonify({'error': 'Invalid credentials'}), 401
        
        access_token = create_access_token(identity=user.id)
        logger.info(f'Successful login for user: {user.email}')
        return jsonify({'token': access_token}), 200
    except Exception as e:
        logger.error(f'Error during login: {str(e)}')
        return jsonify({'error': str(e)}), 400 