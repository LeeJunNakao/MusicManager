import pytest
from pydantic import ValidationError
from unittest.mock import MagicMock, Mock

from domain.user import CreateUserDto
from services import auth_services


@pytest.fixture(name="valid_data")
def valid_data_fixture():
    return {
        "name": "João das Neves",
        "email": "joao_neves@email.com",
        "password": "Sr26_@sd",
    }


@pytest.fixture(name="invalid_data")
def invalid_data_fixture():
    return {
        "email": "joao_neves@emailcom",
        "password": "abc123456",
    }


@pytest.fixture(name="user")
def user_fixture(valid_data):
    user = Mock()
    user.password = auth_services.hash_handler(valid_data["password"])
    user.email = valid_data["email"]
    user.id = 1

    return user


class TestLoginDto:
    def test_create_user_with_valid_data(self, valid_data):
        assert CreateUserDto(**valid_data)

    def test_create_user_with_invalid_email(self, valid_data, invalid_data):
        with pytest.raises(ValidationError):
            assert CreateUserDto(**{**valid_data, "email": invalid_data["email"]})

    def test_create_user_with_invalid_password(self, valid_data, invalid_data):
        with pytest.raises(ValidationError):
            assert CreateUserDto(**{**valid_data, "password": invalid_data["password"]})

    def test_service_create_user(self, valid_data, user):
        session = Mock()
        session.commit = MagicMock()

        repo = Mock()
        repo.create = MagicMock()
        repo.get_one = MagicMock(return_value=user)

        encoded_jwt = auth_services.create_user(session, valid_data, repo)

        assert "token" in encoded_jwt.keys()

    def test_service_validate_token(self, valid_data, user):
        session = Mock()
        session.commit = MagicMock()

        repo = Mock()
        repo.get_one = MagicMock(return_value=user)

        encoded_jwt = auth_services.login(session, valid_data, repo)

        decoded_token = auth_services.validate_token(encoded_jwt["token"])

        assert decoded_token["id"] == user.id
