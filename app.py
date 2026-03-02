

from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity,
)
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# Config
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")

mongo = PyMongo(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

users = mongo.db.users

@app.errorhandler(Exception)
def handle_exception(e):
    print(f"Error occurred: {e}")  
    return jsonify({"error": "Internal server error"}), 500

# Register
@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"msg": "Missing fields"}), 400
    if "@" not in email:
        return jsonify({"msg": "invalid email"}), 400
    if len(password)<8:
        return jsonify({"msg": "short password"}), 400


    if users.find_one({"email": email}):
        return jsonify({"msg": "User already exists"}), 400

    hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

    users.insert_one({
        "email": email,
        "password": hashed_password
    })

    return jsonify({"msg": "User created"}), 201


# Login
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    user = users.find_one({"email": email})

    if not user or not bcrypt.check_password_hash(user["password"], password):
        return jsonify({"msg": "Invalid credentials"}), 401

    access_token = create_access_token(identity=email)

    return jsonify(access_token=access_token), 200


# Protected Route
@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


if __name__ == "__main__":
    app.run(debug=True)