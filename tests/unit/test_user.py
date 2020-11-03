import pytest
from pydantic import ValidationError

from domain.user import CreateUserDto


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


class TestLoginDto:
    def test_create_user_with_valid_data(self, valid_data):
        assert CreateUserDto(**valid_data)

    def test_create_user_with_invalid_email(self, valid_data, invalid_data):
        with pytest.raises(ValidationError):
            assert CreateUserDto(**{**valid_data, "email": invalid_data["email"]})

    def test_create_user_with_invalid_password(self, valid_data, invalid_data):
        with pytest.raises(ValidationError):
            assert CreateUserDto(**{**valid_data, "password": invalid_data["password"]})
