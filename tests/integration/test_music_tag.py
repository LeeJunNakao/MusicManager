import pytest
from faker import Faker
from pydantic import ValidationError

from adapters.database_config import get_session
from services.music_tag_services import create_music_tag


@pytest.fixture(name="valid_data")
def valid_data_fixture():
    return {"name": "Favoritos"}


@pytest.fixture(name="invalid_data")
def invalid_data_fixture():
    return {"name": ""}


class TestMusicTag:
    def test_insert_with_valid_data(self, valid_data, user_info):
        session = get_session()

        music_tag = create_music_tag(
            session, {**valid_data, "user_id": user_info["id"]}
        )

        assert music_tag.name == valid_data["name"]
        assert music_tag.id == user_info["id"]

    def test_insert_with_invalid_data(self, invalid_data, user_info):
        session = get_session()

        with pytest.raises(ValidationError):
            create_music_tag(session, {**invalid_data, "user_id": user_info["id"]})

    def test_insert_with_invalid_user(self, valid_data):
        session = get_session()

        with pytest.raises(Exception):
            create_music_tag(session, {**valid_data, "user_id": 1})