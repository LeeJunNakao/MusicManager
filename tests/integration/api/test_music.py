import pytest
from faker import Faker


@pytest.fixture(name="valid_data")
def valid_data_fixture():
    return {"name": "In the end", "artist": "Linkin Park"}


@pytest.fixture(name="invalid_data")
def invalid_data_fixture():
    return {"name": "", "artist": ""}


@pytest.fixture(name="music_list")
def music_list_fixture():
    fake = Faker()

    return [
        {"name": fake.name(), "artist": fake.name(), "info": fake.address()}
        for _ in range(10)
    ]


class TestMusic:
    endpoint = "/music"

    def test_create_music_with_valid_data(self, app, headers, valid_data):
        with app.test_client() as client:
            response = client.post(self.endpoint, headers=headers, json=valid_data)

        body = response.get_json()
        assert body["id"] == 1
        assert body["name"] == valid_data["name"]
        assert body["artist"] == valid_data["artist"]
        assert body["info"] is None

    def test_create_music_with_invalid_name(
        self, app, headers, valid_data, invalid_data
    ):
        with app.test_client() as client:
            response = client.post(
                self.endpoint,
                headers=headers,
                json={**valid_data, "name": invalid_data["name"]},
            )

        assert (
            response.data.decode("utf-8")
            == "O(s) campo(s) name foram informados incorretamente"
        )
        assert response.status_code == 400

    def test_create_music_with_invalid_artist(
        self, app, headers, valid_data, invalid_data
    ):
        with app.test_client() as client:
            response = client.post(
                self.endpoint,
                headers=headers,
                json={**valid_data, "artist": invalid_data["artist"]},
            )

        assert (
            response.data.decode("utf-8")
            == "O(s) campo(s) artist foram informados incorretamente"
        )
        assert response.status_code == 400

    def test_create_music_without_token(self, app, valid_data):
        with app.test_client() as client:
            response = client.post(self.endpoint, json=valid_data)

        assert response.data.decode("utf-8") == "Favor fazer o login"
        assert response.status_code == 400

    def test_get_music_with_token(self, app, headers, music_list):
        with app.test_client() as client:
            response_list = [
                client.post(self.endpoint, headers=headers, json=music)
                for music in music_list
            ]

        responses_body = [response.get_json() for response in response_list]

        for music in zip(music_list, responses_body):
            assert music[0]["name"] == music[1]["name"]
            assert music[0]["artist"] == music[1]["artist"]
            assert music[0]["info"] == music[1]["info"]

    def test_get_music_without_token(self, app, headers, music_list):
        with app.test_client() as client:
            response_list = [
                client.post(self.endpoint, json=music) for music in music_list
            ]

        for response in response_list:
            assert response.status_code == 400
