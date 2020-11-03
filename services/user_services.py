from adapters.repository import UserRepository
from services.utils.hash import hash_handler
from domain.user import UpdateUserDto


def update_user_data(**data):
    keys = data.keys()

    dto = UpdateUserDto(**data)

    for key in keys:
        if key == "password":
            password = data["password"]
            dto.password = hash_handler(password)

    UserRepository.update_by_id(**dto.dict())

    return "Dados atualizados"

def list_users():
    users = UserRepository.list()
    return [UpdateUserDto(**vars(user)).dict() for user in users]