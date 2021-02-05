from services.utils.hash import hash_handler
from domain.user import UpdateUserDto, GetUserDto
from protocols.repository import UserRepository


def update_user_data(session, data, repo: UserRepository):
    keys = data.keys()

    dto = UpdateUserDto(**data)

    for key in keys:
        if key == "password":
            password = data["password"]
            dto.password = hash_handler(password)
    try:
        repo.update_by_id(session, dto.dict())
        session.commit()
    except Exception:
        session.rollback()
        raise Exception
    finally:
        session.close()

    return "Dados atualizados"


def list_users(repo: UserRepository):
    users = repo.list()
    return [UpdateUserDto(**vars(user)).dict() for user in users]


def find_user(session, data, repo: UserRepository):
    result = repo.get_one(session, dict(**data))
    user = GetUserDto(**vars(result))
    return user.dict()
