from flask import Blueprint, jsonify, request
from models.user import User
from werkzeug.security import check_password_hash
from utils import get_request_header_authorization_token, required_authentification
import secrets
from flask_sieve import validate
from requests.register_request import RegisterRequest
from app import httpauth, bcrypt
auth = Blueprint('auth', __name__) 


@auth.route('/register', methods=['POST'])
@validate(RegisterRequest)
def register():
    user = User.create(request.form)
    return jsonify({
        "message": "Inscription bien effectuée",
        "data": user.serialize()
    })


@auth.route("/login", methods=["POST"])
def login():
    if "email" in request.form.keys() and "password" in request.form.keys():
        user = User.where("email", request.form["email"]).first()
        if user:
            correct_password = bcrypt.check_password_hash(
                user.password, request.form["password"])
            if correct_password:
                token = secrets.token_hex(500)
                user.token = token
                user.save()
                return jsonify({
                    "message": "Vous êtes connecté",
                    "data": user.serialize(),
                    "token": token
                }), 200
            return jsonify({
                "message": "Adresse email ou mot de passe incorecte",
            }), 401
        return jsonify({
            "message": "Adresse email ou mot de passe incorecte"
        }), 401
    return jsonify({
        "message": "Merci de renseigner votre adresse email et votre mot de passe"
    }), 422


@auth.route("/logout")
@httpauth.login_required
def logout():
    httpauth.current_user().update(token=None)
    return jsonify({
        "message": "Vous êtes déconnecté",
    }), 200


@auth.route("/user")
@httpauth.login_required
def user():
    return jsonify({
        "result": httpauth.current_user().serialize()
    }), 200
 
