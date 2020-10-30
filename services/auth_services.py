from domain.user import CreateUserDto, LoginUserDto
from adapters.repository import UserRepository
from services.utils.hash import hash_handler
from services.utils.jwt_token_handler import generate_token, decode_token
import jwt


def create_user(**data):

    unhashed_password = data['password']
    dto = CreateUserDto(**data)
    dto.password = hash_handler(dto.password)
    UserRepository.create(**dto.dict())
    encoded_jwt = login(email=dto.email, password=unhashed_password)

    return encoded_jwt


def login(**data):
    print(data)
    dto = LoginUserDto(**data)
    user = UserRepository.get_one(email=dto.email)
    hashed_password = hash_handler(dto.password)

    if user.password != hashed_password:
        raise Exception

    encoded_jwt = generate_token({"id": user.id})

    return {"token": encoded_jwt.decode("utf-8")}


def validate_token(token):
    return decode_token(token)


# def list_users():
#     users = UserRepository.list()
#     return users