from app import db
from datetime import datetime

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    stripe_payment_id = db.Column(db.String(100), unique=True)
    status = db.Column(db.String(20), nullable=False, default='pending')
    payment_date = db.Column(db.DateTime, default=datetime.utcnow)
    rent_for_month = db.Column(db.Date, nullable=False) 