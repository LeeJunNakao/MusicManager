import pytest
from faker import Faker
from pydantic import ValidationError

from services import music_services
from adapters.database_config import get_session


@pytest.fixture(name="create_valid_data")
def create_valid_data_fixture():
    return {"name": "Take a look around", "artist": "Limp Bizkit", "info": "Nice album"}


@pytest.fixture(name="create_invalid_data")
def create_invalid_data_fixture():
    return {"name": "", "artist": None}


@pytest.fixture(name="create_valid_data_list")
def create_valid_data_list_fixture():
    fake = Faker()

    musics = []

    for _ in range(20):
        music = {
            "user_id": 1,
            "name": fake.name(),
            "artist": fake.name(),
            "info": fake.name(),
        }
        musics.append(music)

    return musics


class TestServices:
    def test_insert_music_with_valid_data(self, create_valid_data, user_info):
        session = get_session()

        music = music_services.insert_music(
            session, {**create_valid_data, "user_id": user_info["id"]}
        )

        assert music["name"] == create_valid_data["name"]
        assert music["artist"] == create_valid_data["artist"]
        assert music["info"] == create_valid_data["info"]

    def test_insert_music_with_invalid_name(
        self, create_valid_data, create_invalid_data, user_info
    ):
        session = get_session()

        with pytest.raises(ValidationError):
            music_services.insert_music(
                session,
                {
                    **create_valid_data,
                    "name": create_invalid_data["name"],
                    "user_id": user_info["id"],
                },
            )

    def test_insert_music_with_invalid_artist(
        self, create_valid_data, create_invalid_data, user_info
    ):
        session = get_session()

        with pytest.raises(ValidationError):
            music_services.insert_music(
                session,
                {
                    **create_valid_data,
                    "artist": create_invalid_data["artist"],
                    "user_id": user_info["id"],
                },
            )

    def test_insert_music_with_invalid_user_id(
        self, create_valid_data, create_invalid_data, user_info
    ):
        session = get_session()

        with pytest.raises(Exception):
            music_services.insert_music(
                session,
                {
                    **create_valid_data,
                    "user_id": 17,
                },
            )

    def test_list_musics_with_valid_data(self, create_valid_data_list, user_info):
        session = get_session()

        for music in create_valid_data_list:
            music_services.insert_music(session, music)

        musics = music_services.list_user_musics(session, user_info["id"])

        for music_arg, music_added in zip(create_valid_data_list, musics):
            assert music_arg["name"] == music_added["name"]
            assert music_arg["artist"] == music_added["artist"]
            assert music_arg["info"] == music_added["info"]
