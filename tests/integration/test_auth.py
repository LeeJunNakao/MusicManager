import pytest
from pydantic import ValidationError
from adapters.repository import UserRepository
from adapters.orm.user import User
from services import auth_services
from adapters.database_config import get_session


@pytest.fixture(name="create_valid_data")
def create_valid_data_fixture():
    return {
        "name": "João",
        "email": "joao@email.com",
        "password": "Abc123@",
    }


@pytest.fixture(name="create_invalid_data")
def create_invalid_data_fixture():
    return {
        "name": "",
        "email": "joao@emailcom",
        "password": "abc123zrt",
    }


@pytest.fixture(name="update_valid_data")
def update_valid_data_fixture():
    return {"id": 1, "name": "João da Silva"}


class TestAuthentication:
    def test_create_user_with_valid_data(self, create_valid_data):
        session = get_session()

        auth_services.create_user(session, **create_valid_data)
        user = UserRepository.get_one(session, name=create_valid_data["name"])

        assert user.name == create_valid_data["name"]

    def test_create_user_with_invalid_email(
        self, create_valid_data, create_invalid_data
    ):
        session = get_session()

        with pytest.raises(ValidationError):
            auth_services.create_user(
                session, **{**create_valid_data, "email": create_invalid_data["email"]}
            )

    def test_create_user_with_invalid_password(
        self, create_valid_data, create_invalid_data
    ):
        session = get_session()

        with pytest.raises(ValidationError):
            auth_services.create_user(
                session,
                **{**create_valid_data, "password": create_invalid_data["password"]}
            )

    def test_create_user_with_invalid_name(
        self, create_valid_data, create_invalid_data
    ):
        session = get_session()

        with pytest.raises(ValidationError):
            auth_services.create_user(
                session, **{**create_valid_data, "name": create_invalid_data["name"]}
            )

    def test_create_user_with_existing_email(self, create_valid_data):
        self.test_create_user_with_valid_data(create_valid_data)

        with pytest.raises(Exception):
            self.test_create_user_with_valid_data(
                {**create_valid_data, "name": "Pedro de Oliveira"}
            )

    def test_register_with_valid_data(self, create_valid_data):
        session = get_session()

        encoded_jwt = auth_services.create_user(session, **create_valid_data)
        decoded_token = auth_services.validate_token(encoded_jwt["token"])

        assert decoded_token["id"] == 1

    def test_login_with_valid_data(self, create_valid_data):
        session = get_session()

        self.test_register_with_valid_data(create_valid_data)
        response = auth_services.login(session, **create_valid_data)

        assert "token" in response.keys()

    def test_login_with_invalid_password(self, create_valid_data):
        session = get_session()

        self.test_register_with_valid_data(create_valid_data)

        with pytest.raises(Exception):
            auth_services.login(
                session, **{**create_valid_data, "password": "A1bc5d5s@"}
            )

    def test_login_with_invalid_email(self, create_valid_data, create_invalid_data):
        session = get_session()

        self.test_register_with_valid_data(create_valid_data)

        with pytest.raises(Exception):
            auth_services.login(
                session, **{**create_valid_data, "email": create_invalid_data["email"]}
            )
