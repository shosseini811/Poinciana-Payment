from app import create_app, db
from app.models.user import User
from app.models.payment import Payment
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = create_app()

def init_db():
    with app.app_context():
        try:
            # Create all tables
            db.create_all()
            print("Database tables created successfully!")
            
            # Print the database URL being used (without password)
            db_url = app.config['SQLALCHEMY_DATABASE_URI']
            safe_db_url = db_url.replace(db_url.split('@')[0], '***')
            print(f"Using database: {safe_db_url}")
            
        except Exception as e:
            print(f"Error creating database tables: {str(e)}")
            raise

if __name__ == '__main__':
    init_db() 