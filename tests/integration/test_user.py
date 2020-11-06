import pytest
from services import auth_services, user_services
from adapters.database_config import get_session


@pytest.fixture(name="create_valid_data")
def create_valid_data_fixture():
    return {
        "name": "João",
        "email": "joao@email.com",
        "password": "Abc123@",
    }


@pytest.fixture(name="update_valid_data")
def update_valid_data_fixture():
    return {
        "name": "João da Silva",
        "email": "joao_silva@email.com",
        "password": "Senha14_@",
    }


class TestUserServices:
    def test_update_valid_data(self, create_valid_data, update_valid_data):
        session = get_session()
        encoded_jwt = auth_services.create_user(session, **create_valid_data)
        user_info = auth_services.validate_token(encoded_jwt["token"])
        user_services.update_user_data(
            session, {**update_valid_data, "id": user_info["id"]}
        )
        user = user_services.find_user(session, {"id": user_info["id"]})

        assert user["name"] == update_valid_data["name"]
        assert user["email"] == update_valid_data["email"]
