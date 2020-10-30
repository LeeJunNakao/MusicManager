from domain.user import CreateUserDto, LoginUserDto
from adapters.repository import UserRepository
from services.utils.hash import hash_handler
from services.utils.jwt_token_handler import generate_token, decode_token
import jwt


def create_user(**data):

    dto = CreateUserDto(**data)
    dto.password = hash_handler(dto.password)
    UserRepository.create(**dto.dict())

    return dto.dict()


def login(**data):

    dto = LoginUserDto(**data)
    user = UserRepository.get_one(email=dto.email)
    hashed_password = hash_handler(dto.password)

    encoded_jwt = generate_token({"id": user.id})

    if user.password != hashed_password:
        raise Exception

    return {"token": encoded_jwt.decode("utf-8")}


def validate_token(token):
    return decode_token(token)

# def list_users():
#     users = UserRepository.list()
#     return users