import pytest

from adapters.database_config import get_session
from services import auth_services
from adapters.repository import UserRepository

@pytest.fixture(name="headers")
def get_valid_user_fixture():
    user_data = {
        "name": "Pedro",
        "email": "pedro@gmail.com",
        "password": "Abc123@",
    }
    session = get_session()
    jwt = auth_services.create_user(session, user_data, UserRepository)

    return jwt
