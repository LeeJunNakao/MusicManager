import pytest
from faker import Faker
from pydantic import ValidationError

from services import music_services, music_tag_services
from adapters.database_config import get_session
from adapters.repository import MusicRepository, MusicTagRepository
from adapters.repository import UserRepository
from adapters.orm.music import Music
from domain.music import Music as MusicDto


@pytest.fixture(name="create_valid_data")
def create_valid_data_fixture():
    return {
        "name": "Take a look around",
        "artist": "Limp Bizkit",
        "album": "Chocolate Starfish",
        "info": "Nice album",
    }


@pytest.fixture(name="create_invalid_data")
def create_invalid_data_fixture():
    return {"name": "", "artist": None, "album": ""}


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


@pytest.fixture(name="create_valid_data_music_tag")
def create_valid_data_music_tag_fixture():
    return {"name": "Favorite"}


@pytest.fixture(name="create_invalid_data_music_tag")
def create_invalid_data_music_tag():
    return {"name": ""}


class TestServices:
    def test_insert_music_with_valid_data(self, create_valid_data, user_info):
        session = get_session()

        music = music_services.insert_music(
            session, {**create_valid_data, "user_id": user_info["id"]}, MusicRepository
        )

        assert music.name == create_valid_data["name"]
        assert music.artist == create_valid_data["artist"]
        assert music.info == create_valid_data["info"]

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
                MusicRepository,
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
                MusicRepository,
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
                MusicRepository,
            )

    def test_list_musics_with_valid_data(self, create_valid_data_list, user_info):
        session = get_session()

        for music in create_valid_data_list:
            music_services.insert_music(session, music, MusicRepository)

        musics = music_services.list_user_musics(
            session, user_info["id"], UserRepository
        )

        for music_arg, music_added in zip(create_valid_data_list, musics):
            assert music_arg["name"] == music_added.name
            assert music_arg["artist"] == music_added.artist
            assert music_arg["info"] == music_added.info


class TestMusicTagIntegration:
    def test_create_music_with_valid_tag(
        self, create_valid_data, create_valid_data_music_tag, user_info
    ):
        session = get_session()

        tag = music_tag_services.create_music_tag(
            session,
            {**create_valid_data_music_tag, "user_id": user_info["id"]},
            MusicTagRepository,
        )

        music = music_services.insert_music(
            session,
            {**create_valid_data, "user_id": user_info["id"], "tag_id": tag.id},
            MusicRepository,
        )

        assert music.name == create_valid_data["name"]
        assert music.artist == create_valid_data["artist"]
        assert music.info == create_valid_data["info"]
        assert music.album == create_valid_data["album"]
        assert music.tag_id == tag.id

    def test_create_music_with_invalid_tag(self, create_valid_data, user_info):
        session = get_session()

        with pytest.raises(Exception):
            music_services.insert_music(
                session, {**create_valid_data, "user_id": user_info["id"], "tag_id": 1}
            )
