from adapters.repository import UserRepository
from services.utils.hash import hash_handler
from domain.user import UpdateUserDto, GetUserDto


def update_user_data(session, data):
    keys = data.keys()

    dto = UpdateUserDto(**data)

    for key in keys:
        if key == "password":
            password = data["password"]
            dto.password = hash_handler(password)
    try:
        UserRepository.update_by_id(session, **dto.dict())
        session.commit()
    except Exception:
        session.rollback()
        raise Exception
    finally:
        session.close()

    return "Dados atualizados"


def list_users():
    users = UserRepository.list()
    return [UpdateUserDto(**vars(user)).dict() for user in users]


def find_user(session, data):
    result = UserRepository.get_one(session, **data)
    user = GetUserDto(**vars(result))
    return user.dict()
