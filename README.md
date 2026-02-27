# 🔐 Authentication API (Flask + MongoDB)

A simple but production-oriented authentication system built with Flask.

## 🚀 Features
- User registration
- Secure password hashing using bcrypt
- JWT-based authentication
- Protected route example
- MongoDB integration

## 🛠 Tech Stack
- Python (Flask)
- MongoDB
- Flask-JWT-Extended
- Flask-Bcrypt

## 🔐 Security
- Passwords are hashed using bcrypt (with automatic salt)
- JWT signed with secret key
- Environment variables for sensitive data

## 📚 What I Learned
- Difference between hashing and encryption
- Why password hashing must be slow
- How JWT identity is extracted in protected routes
- Structuring a minimal backend API

## ▶️ Run Locally
1. Create virtual environment
2. Install requirements
3. Add `.env`
4. Run `python app.py`