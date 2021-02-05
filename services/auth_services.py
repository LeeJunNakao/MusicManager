from domain.user import CreateUserDto, LoginUserDto, User
from services.utils.hash import hash_handler
from services.utils.jwt_token_handler import generate_token, decode_token
from protocols.repository import UserRepository
from services.utils.exceptions import PersistenceError, LoginError


def create_user(session, data: dict, repo: UserRepository) -> dict:
    unhashed_password = data["password"]
    create_dto = CreateUserDto(**data)
    create_dto.password = hash_handler(create_dto.password)
    user_data = create_dto.dict()

    try:
        repo.create(session, user_data)
        session.commit()
    except Exception:
        session.rollback()
        raise PersistenceError("User")
    finally:
        session.close()

    encoded_jwt = login(
        session,
        {"email": create_dto.email, "password": unhashed_password},
        repo,
    )

    return encoded_jwt


def login(session, data, repo: UserRepository) -> dict:
    dto = LoginUserDto(**data)
    try:
        user = repo.get_one(session, dict(email=dto.email))
        hashed_password = hash_handler(dto.password)

        if user.password != hashed_password:
            raise Exception()

        encoded_jwt = generate_token({"id": user.id})

        return {"token": encoded_jwt.decode("utf-8")}
    except Exception:
        raise LoginError


def validate_token(token) -> dict:
    return decode_token(token)
