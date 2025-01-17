# Poinciana Payment System

A modern payment management system for handling rental payments at Poinciana Properties. Built with Flask and vanilla JavaScript, this application provides a simple and secure experience for processing and managing rental payments.

## Features

- Secure user authentication and authorization
- Simple payment submission system
- Payment history tracking
- User registration and login
- Secure payment status monitoring

## Tech Stack

### Backend
- Python/Flask
- PostgreSQL Database
- SQLAlchemy ORM
- JWT Authentication
- Flask-CORS for cross-origin handling

### Frontend
- Vanilla JavaScript
- HTML5/CSS3
- Fetch API for backend communication

## Setup and Installation

1. Clone the repository
```bash
git clone https://github.com/[your-username]/poinciana-payment.git
cd poinciana-payment
```

2. Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Frontend Setup
```bash
cd frontend
npm install
```

4. Database Setup
- Install PostgreSQL if not already installed
- Create a new database named `rent_payment_db`
- Update the database connection details in `.env`

5. Environment Configuration
Create a `.env` file in the backend directory with the following variables:
```
DATABASE_URL="postgresql://postgres:your_password@localhost:5432/rent_payment_db"
SECRET_KEY="your-secret-key-here"
JWT_SECRET_KEY="your-jwt-secret-key-here"
FLASK_APP=run.py
FLASK_ENV=development
```

6. Initialize the Database
```bash
cd backend
python init_db.py
```

## Running the Application

1. Start the Backend Server
```bash
cd backend
source venv/bin/activate
python run.py
```
The backend will run on `http://localhost:8001`

2. Start the Frontend Server
```bash
cd frontend
npm start
```
The frontend will be available at `http://localhost:3000/public/index.html`

## Project Structure

```
poinciana-payment/
├── backend/
│   ├── app/
│   │   ├── models/
│   │   ├── routes/
│   │   └── __init__.py
│   ├── venv/
│   ├── config.py
│   ├── init_db.py
│   ├── requirements.txt
│   └── run.py
└── frontend/
    ├── public/
    │   └── index.html
    └── src/
        ├── css/
        └── js/
            ├── auth.js
            ├── payment.js
            └── utils.js
```

## API Endpoints

- POST `/register` - User registration
- POST `/login` - User authentication
- POST `/submit-payment` - Submit payment information
- GET `/payment-history` - Get user's payment history

## Security Notes

- All sensitive credentials are stored in environment variables
- JWT is used for authentication
- Passwords are hashed before storage
- CORS is configured for security
- Never commit `.env` files or any files containing sensitive information

## Development Notes

- The backend runs in debug mode for development
- Frontend uses no-cors mode for API requests
- Database migrations are handled through SQLAlchemy
- Logging is implemented for debugging and monitoring

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.