from orator import Model


class User(Model):
    __fillable__ = ["email", "password", "token"]
    __hidden__ = ["password"]
