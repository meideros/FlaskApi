from flask import request

from models.user import User

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'tif'}
UPLOAD_FOLDER = "static/"
regexEmail = '^[a-z0-9._-]+@[a-z0-9._-]+\.[a-z]{2,6}$'
regexPhoneNumber = '^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'


def user_is_authorized(token):
    if token is not None:
        user = User.where('token', token).first()
        if user:
            return True
        return False
    return False


def get_request_header_authorization_token():
    if 'Authorization' in request.headers.keys():
        return request.headers.get("Authorization").split(" ")[1]
    return None


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS