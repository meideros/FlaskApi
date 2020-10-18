from flask_sieve import FormRequest


class RegisterRequest(FormRequest):

    def rules(self):
        return {
            'email': ['required', 'email'],
            'password': ['required', 'min:6']
        }

    def messages(self):
        return {
            'email.required': 'The email is required',
            'password': 'The password is required',
            'password.min': 'The password is too shurt'

        }



