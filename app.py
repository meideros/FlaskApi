from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_orator import Orator
from flask_sieve import Sieve
from flask_mail import Mail, Message
from models.user import User
from werkzeug.security import generate_password_hash
from config import BaseConfig
from flask_httpauth import HTTPTokenAuth
from flask_bcrypt import Bcrypt

app = Flask(__name__)
httpauth = HTTPTokenAuth(scheme='Bearer')

app.config.from_object(BaseConfig)

CORS(app)
Sieve(app)
mail = Mail(app)
db = Orator(app)
bcrypt = Bcrypt(app)
from api.auth import auth
app.register_blueprint(auth, url_prefix="/api/auth")


@app.route('/')
def index():
    return jsonify({
        "message": "Hello word",
    })


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify({
        "message": str(e),
    }), 404


@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify({
        "message": str(e),
    }), 405


@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({
        "message": str(e),
    }), 500


@httpauth.verify_token
def verify_token(token):
   return User.where('token', token).first()


@httpauth.error_handler
def auth_error(status):
    return jsonify({
        "message": "Non authorisé. Merci de renseigner un token d'authorisation valide"
    }), status
if __name__ == "__main__":
    app.run(debug=True)
