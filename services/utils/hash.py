import hashlib
import os


def hash_handler(password):

    salt = os.getenv("HASH_SALT").encode("utf-8")
    new_password = hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), salt, 100000, dklen=128
    )
    return new_password.hex()
