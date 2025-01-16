from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from config import Config

# Initialize extensions
db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize extensions with app
    db.init_app(app)
    jwt.init_app(app)
    
    # Register blueprints
    from app.routes.auth import auth_bp
    from app.routes.payments import payments_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(payments_bp)
    
    return app 