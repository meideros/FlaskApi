from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_orator import Orator
from flask_sieve import Sieve
from flask_mail import Mail, Message


app = Flask(__name__)
app.config['MAIL_SERVER'] = 'your_mail_serveur'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'your_username'
app.config['MAIL_PASSWORD'] = 'your_password'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
ORATOR_DATABASES = {
    'mysql': {
        'driver': 'mysql',
        'host': 'server_address',
        'database': 'database_name',
        'user': 'your_username',
        'password': 'your_password',
        'prefix': ''
    }
}
app.config.from_object(__name__)


CORS(app)
Sieve(app)
mail = Mail(app)
db = Orator(app)




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


if __name__ == "__main__":
    app.run(debug=False, port=3000)
