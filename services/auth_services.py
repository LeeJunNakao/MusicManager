from domain.user import CreateUserDto, LoginUserDto
from adapters.repository import UserRepository
from services.utils.hash import hash_handler
from services.utils.jwt_token_handler import generate_token, decode_token


def create_user(session, **data):
    unhashed_password = data["password"]
    dto = CreateUserDto(**data)
    dto.password = hash_handler(dto.password)

    try:
        UserRepository.create(session, **dto.dict())
        session.commit()
    except Exception:
        session.rollback()
        raise Exception
    finally:
        session.close()

    encoded_jwt = login(session, email=dto.email, password=unhashed_password)

    return encoded_jwt


def login(session, **data):
    dto = LoginUserDto(**data)
    user = UserRepository.get_one(session, email=dto.email)
    hashed_password = hash_handler(dto.password)

    if user.password != hashed_password:
        raise Exception

    encoded_jwt = generate_token({"id": user.id})

    return {"token": encoded_jwt.decode("utf-8")}


def validate_token(token):
    return decode_token(token)
