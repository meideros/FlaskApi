from flask import Blueprint, jsonify, request
from models.user import User
from werkzeug.security import check_password_hash
from utils import get_request_header_authorization_token, required_authentification
import secrets

auth = Blueprint('auth', __name__)


@auth.route("/login", methods=["POST"])
def login():
    if "email" in request.form.keys() and "password" in request.form.keys():
        user = User.where("email", request.form["email"]).first()
        if user:
            correct_password = check_password_hash(user.password, request.form["password"])
            if correct_password:
                user.token = secrets.token_hex(100)
                user.save()
                return jsonify({
                    "message": "Vous êtes connecté",
                    "data": user.serialize()
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
@required_authentification
def logout():
    User.where('token', get_request_header_authorization_token()).update(token=None)
    return jsonify({
        "message": "Vous êtes déconnecté",
    }), 200


@auth.route("/user")
@required_authentification
def user():
    return jsonify({
        "result": User.where('token', get_request_header_authorization_token()).first(),
    }), 200
