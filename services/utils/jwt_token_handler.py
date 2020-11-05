import os
import jwt
import time

from config import get_settings

settings = get_settings()


def generate_token(data):
    secret = settings.JWT_SECRET
    algorithm = "HS256"
    one_day_in_seconds = 86400
    now = time.time()
    expiration_time = now + one_day_in_seconds
    return jwt.encode({**data, "exp": expiration_time}, secret, algorithm=algorithm)


def decode_token(token):
    secret = settings.JWT_SECRET
    algorithms = ["HS256"]

    return jwt.decode(token, secret, algorithms=algorithms)
