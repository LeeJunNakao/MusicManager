from functools import wraps
from flask import request
from services.auth_services import validate_token


def login_required(f):
    @wraps(f)
    def verify_token(*args, **kwargs):
        try:
            token = request.headers["Token"]
            decoded_token = validate_token(token)
            request.user_info = decoded_token
            return f(*args, **kwargs)
        except:
            return "Favor fazer o login", 400

    return verify_token
