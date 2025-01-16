# Poinciana Payment System

A modern, secure payment management system for handling rental payments at Poinciana Properties. Built with Flask and React, this application provides a seamless experience for processing and managing rental payments.

## Features

- Secure user authentication and authorization
- Automated rental payment processing via Stripe
- Payment history tracking and management
- Monthly rent payment scheduling
- Secure payment status monitoring

## Tech Stack

### Backend
- Python/Flask
- SQLAlchemy ORM
- JWT Authentication
- Stripe Payment Integration

### Frontend
- React.js
- Material-UI
- Axios for API calls

## Setup and Installation

1. Clone the repository
```bash
git clone https://github.com/[your-username]/Poinciana-Payment.git
cd Poinciana-Payment
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

4. Environment Configuration
- Create a `.env` file in the backend directory
- Add required environment variables (see `.env.example`)

## Running the Application

1. Start the Backend Server
```bash
cd backend
flask run
```

2. Start the Frontend Development Server
```bash
cd frontend
npm start
```

## Security Notes

- All sensitive credentials should be stored in environment variables
- Never commit `.env` files or any files containing sensitive information
- Always use environment-specific configuration files

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.