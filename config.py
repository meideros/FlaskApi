class BaseConfig(object):
    MAIL_SERVER = '127.0.0.1'
    MAIL_PORT = 1025
    MAIL_USERNAME = ""
    MAIL_PASSWORD = ""
    MAIL_USE_TLS = False
    MAIL_USE_SSL = False
    JSON_SORT_KEYS = False
    UPLOAD_FOLDER = "static/upload"
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


class DevConfig(object):
    MAIL_SERVER = '127.0.0.1'
    MAIL_PORT = 1025
    MAIL_USERNAME = ""
    MAIL_PASSWORD = ""
    MAIL_USE_TLS = False
    SIEVE_RESPONSE_MESSAGE = "Invalide"
    SIEVE_INCLUDE_SUCCESS_KEY = False
    MAIL_USE_SSL = False
    JSON_SORT_KEYS = False
    UPLOAD_FOLDER = "static/upload"
    ORATOR_DATABASES = {
        'mysql': {
            'driver': 'mysql',
            'host': 'localhost',
            'database': 'test',
            'user': 'root',
            'password': 'root',
            'prefix': ''
        }
    }
