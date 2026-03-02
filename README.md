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

## 🛡 Security Considerations

This project implements user authentication using **bcrypt** and **JWT (JSON Web Tokens)** to ensure security best practices.

### 1️⃣ Why bcrypt + JWT?

- **bcrypt** is used to hash passwords before storing them in the database.
  - Hashing is **one-way**: the original password cannot be retrieved from the hash.
  - bcrypt automatically applies **salting** and is **computationally slow**, which protects against brute-force and rainbow table attacks.
- **JWT** is used for session management.
  - Once the user logs in, they receive a JWT token.
  - The token is signed with a secret key (`JWT_SECRET_KEY`), so the server can verify its integrity.
  - JWT allows stateless authentication: the server does not need to store session data.

### 2️⃣ What problem salting solves?

- Salting adds a random string to each password before hashing.
- Without salt, two users with the same password would have the same hash, making attacks easier.
- Salting ensures that even if two users have the same password, their stored hashes are **different**.
- It also prevents precomputed attacks like **rainbow table attacks**.

### 3️⃣ Summary

- Never store passwords in plain text.
- Use bcrypt for secure password hashing.
- Use JWT for stateless and secure user authentication.
- Always use salt to protect against precomputed hash attacks.

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