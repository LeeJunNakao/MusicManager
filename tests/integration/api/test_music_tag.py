import pytest
from faker import Faker

MOCK_QUANTITY = 10


@pytest.fixture(name="valid_data")
def valid_data_fixture():
    return {
        "name": "Rock",
    }


@pytest.fixture(name="invalid_data")
def invalid_data_fixture():
    return {
        "name": "",
    }


@pytest.fixture(name="update_valid_data")
def update_valid_data_fixture():
    return {
        "name": "Hard Rock",
    }


def create_music_tag(app, headers, data, ctx):
    with app.test_client() as client:
        response = client.post(
            ctx.endpoint,
            headers=headers,
            json=data,
        )

    return response


@pytest.fixture(name="music_tag_list")
def music_tag_list_fixture():
    fake = Faker()

    return [{"name": fake.name()} for _ in range(MOCK_QUANTITY)]


class TestMusicTag:
    endpoint = "/music_tag"

    def test_create_with_valid_data(self, app, valid_data, headers):
        response = create_music_tag(app, headers, valid_data, self)
        body = response.get_json()

        assert body["name"] == valid_data["name"]
        assert response.status_code == 201

    def test_create_with_invalid_name(self, app, valid_data, invalid_data, headers):
        response = create_music_tag(
            app, headers, {**valid_data, "name": invalid_data["name"]}, self
        )

        assert response.data.decode("utf-8") == "Não foi possível criar tag"
        assert response.status_code == 400

    def test_update_with_valid_data(self, app, valid_data, update_valid_data, headers):
        post_response = create_music_tag(app, headers, valid_data, self)
        post_body = post_response.get_json()
        tag_id = post_body["id"]

        with app.test_client() as client:
            response = client.put(
                f"{self.endpoint}/{tag_id}",
                headers=headers,
                json=update_valid_data,
            )

        body = response.get_json()

        assert body["name"] == update_valid_data["name"]
        assert body["id"] == tag_id
        assert response.status_code == 200

    def test_update_with_invalid_name(
        self, app, valid_data, update_valid_data, invalid_data, headers
    ):
        post_response = create_music_tag(app, headers, valid_data, self)
        post_body = post_response.get_json()
        tag_id = post_body["id"]

        with app.test_client() as client:
            response = client.put(
                f"{self.endpoint}/{tag_id}",
                headers=headers,
                json={**update_valid_data, "name": invalid_data["name"]},
            )

        assert response.data.decode("utf-8") == "Não foi possível atualizar tag"
        assert response.status_code == 400

    def test_get_with_valid_token(self, app, headers, music_tag_list):
        for music_tag in music_tag_list:
            create_music_tag(app, headers, music_tag, self)

        with app.test_client() as client:
            response = client.get(self.endpoint, headers=headers)

        body = response.get_json()

        assert len(body) == MOCK_QUANTITY
        for tag, source in zip(body, music_tag_list):
            assert tag["name"] == source["name"]
        assert response.status_code == 200

    def test_get_without_valid_token(self, app, headers, music_tag_list):
        for music_tag in music_tag_list:
            create_music_tag(app, headers, music_tag, self)

        with app.test_client() as client:
            response = client.get(self.endpoint)
        
        assert response.data.decode("utf-8") == "Favor fazer o login"
        assert response.status_code == 400
