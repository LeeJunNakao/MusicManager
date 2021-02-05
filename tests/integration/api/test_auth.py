import pytest
from services.utils.exceptions import PersistenceError, LoginError
from api.utils import exceptions


@pytest.fixture(name="valid_data")
def valid_data_fixture():
    return {
        "name": "Marcio Ribeiro",
        "email": "marcio_ribeiro@hotmail.com",
        "password": "Ysd24@21f",
    }


@pytest.fixture(name="invalid_data")
def invalid_data_fixture():
    return {"name": "", "email": "email.email.com", "password": "password123"}


class TestRegister:
    endpoint = "/auth/register"

    def test_register_with_valid_data(self, app, valid_data):
        with app.test_client() as client:
            response = client.post(self.endpoint, json=valid_data)

        body = response.get_json()
        assert body["token"] is not None
        assert response.status_code == 201

    def test_register_with_invalid_name(self, app, valid_data, invalid_data):
        with app.test_client() as client:
            response = client.post(
                self.endpoint,
                json={**valid_data, "name": invalid_data["name"]},
            )

        body = response.get_json()
        assert body is None
        assert response.status_code == 400

    def test_register_with_invalid_email(self, app, valid_data, invalid_data):
        with app.test_client() as client:
            response = client.post(
                self.endpoint,
                json={**valid_data, "email": invalid_data["email"]},
            )

        body = response.get_json()
        assert body is None
        assert response.status_code == 400

    def test_register_with_invalid_password(self, app, valid_data, invalid_data):
        with app.test_client() as client:
            response = client.post(
                self.endpoint,
                json={
                    **valid_data,
                    "password": invalid_data["password"],
                },
            )

        body = response.get_json()
        assert body is None
        assert response.status_code == 400


class TestLogin:
    endpoint = "/auth/login"

    def test_login_with_valid_data(self, app, valid_data):
        with app.test_client() as client:
            client.post("/auth/register", json=valid_data)

        with app.test_client() as client:
            response = client.post(
                self.endpoint,
                json=valid_data,
            )

        body = response.get_json()
        assert body["token"] is not None
        assert response.status_code == 200

    def test_login_with_wrong_email(self, app, valid_data, invalid_data):
        with app.test_client() as client:
            client.post("/auth/register", json=valid_data)

        with app.test_client() as client:
            response = client.post(
                self.endpoint,
                json={**valid_data, "email": "mercio@hotmail.com"},
            )

        assert response.data.decode("utf-8") == LoginError().message
        assert response.status_code == 400

    def test_login_with_wrong_password(self, app, valid_data, invalid_data):
        with app.test_client() as client:
            client.post("/auth/register", json=valid_data)

        with app.test_client() as client:
            response = client.post(
                self.endpoint,
                json={**valid_data, "password": "Marc12@15"},
            )

        assert response.data.decode("utf-8") == LoginError().message
        assert response.status_code == 400

    def test_login_with_invalid_email(self, app, valid_data, invalid_data):
        with app.test_client() as client:
            client.post("/auth/register", json=valid_data)

        with app.test_client() as client:
            response = client.post(
                self.endpoint,
                json={**valid_data, "email": invalid_data["email"]},
            )

        assert response.data.decode("utf-8") == exceptions.auth_validation_error
        assert response.status_code == 400

    def test_login_with_invalid_email(self, app, valid_data, invalid_data):
        with app.test_client() as client:
            client.post("/auth/register", json=valid_data)

        with app.test_client() as client:
            response = client.post(
                self.endpoint,
                json={**valid_data, "password": invalid_data["password"]},
            )

        assert response.data.decode("utf-8") == exceptions.auth_validation_error
        assert response.status_code == 400
