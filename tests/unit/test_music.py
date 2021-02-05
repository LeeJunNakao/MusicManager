import pytest
from pydantic import ValidationError
from unittest.mock import MagicMock, Mock

from domain.music import (
    InsertMusicDto,
    GetMusicDto,
    InsertMusicTagDto,
    GetMusicTagDto,
    Music,
)
from domain.user import User
from domain.music import MusicTag
from services import music_services, music_tag_services


@pytest.fixture(name="create_valid_data")
def create_valid_data_fixture():
    return {
        "user_id": 7,
        "tag_id": 255,
        "name": "Californication",
        "album": "Californication",
        "artist": "Red Hot Chilli Peppers",
        "info": "nice song",
    }


@pytest.fixture(name="create_invalid_data")
def crate_invalid_data_fixture():
    return {
        "user_id": "ten",
        "name": "",
        "artist": "",
        "album": "",
        "tag_id": "Favorite",
    }


@pytest.fixture(name="get_valid_data")
def get_valid_data_fixture():
    return {
        "id": 255,
        "name": "Everlong",
        "artist": "Foo Fighters",
        "album": "The Colour and the Shape",
        "info": "nice",
    }


@pytest.fixture(name="get_invalid_data")
def get_invalid_data_fixture():
    return {"id": None, "name": "", "artist": "", "album": "", "tag_id": "Favorites"}


@pytest.fixture(name="create_music_tag_valid_data")
def create_music_tag_valid_data_fixture():
    return {"user_id": 5, "name": "Favorite"}


@pytest.fixture(name="create_music_tag_invalid_data")
def create_music_tag_invalid_data_fixture():
    return {"user_id": None, "name": "dddddddddddddddddddddddddddddddddddddddddddd"}


@pytest.fixture(name="get_music_tag_valid_data")
def get_music_tag_valid_data_fixture():
    return {"id": 99, "user_id": 5, "name": "Favorite"}


@pytest.fixture(name="get_music_tag_invalid_data")
def get_music_tag_invalid_data_fixture():
    return {"user_id": "a hundread", "name": None}


class TestMusicDto:
    def test_insert_with_valid_data(self, create_valid_data):
        assert InsertMusicDto(**create_valid_data)

    def test_insert_music_with_invalid_user_id(
        self, create_valid_data, create_invalid_data
    ):
        with pytest.raises(ValidationError):
            assert InsertMusicDto(
                **{**create_valid_data, "user_id": create_invalid_data["user_id"]}
            )

    def test_insert_music_with_invalid_name(
        self, create_valid_data, create_invalid_data
    ):
        with pytest.raises(ValidationError):
            assert InsertMusicDto(
                **{**create_valid_data, "name": create_invalid_data["name"]}
            )

    def test_insert_music_with_invalid_artist(
        self, create_valid_data, create_invalid_data
    ):
        with pytest.raises(ValidationError):
            assert InsertMusicDto(
                **{**create_valid_data, "artist": create_invalid_data["artist"]}
            )

    def test_insert_music_with_invalid_tag_id(
        self, create_valid_data, create_invalid_data
    ):
        with pytest.raises(ValidationError):
            assert InsertMusicDto(
                **{**create_valid_data, "tag_id": create_invalid_data["tag_id"]}
            )

    def test_insert_music_with_invalid_album(
        self, create_valid_data, create_invalid_data
    ):
        with pytest.raises(ValidationError):
            assert InsertMusicDto(
                **{**create_valid_data, "album": create_invalid_data["album"]}
            )

    def test_insert_music_with_no_info(self, create_valid_data, create_invalid_data):
        assert InsertMusicDto(**{**create_valid_data, "info": None})

    def test_get_music_with_valid_data(self, get_valid_data):
        assert GetMusicDto(**get_valid_data)

    def test_get_music_with_invalid_id(self, get_valid_data, get_invalid_data):
        with pytest.raises(ValidationError):
            assert GetMusicDto(**{**get_valid_data, "id": get_invalid_data["id"]})

    def test_get_music_with_invalid_name(self, get_valid_data, get_invalid_data):
        with pytest.raises(ValidationError):
            assert GetMusicDto(**{**get_valid_data, "name": get_invalid_data["name"]})

    def test_get_music_with_invalid_artist(self, get_valid_data, get_invalid_data):
        with pytest.raises(ValidationError):
            assert GetMusicDto(
                **{**get_valid_data, "artist": get_invalid_data["artist"]}
            )

    def test_create_music_tag_with_valid_data(self, create_music_tag_valid_data):
        assert InsertMusicTagDto(**create_music_tag_valid_data)

    def test_create_music_tag_with_invalid_user_id(
        self, create_music_tag_valid_data, create_music_tag_invalid_data
    ):
        with pytest.raises(ValidationError):
            assert InsertMusicTagDto(
                **{
                    **create_music_tag_valid_data,
                    "user_id": create_music_tag_invalid_data["user_id"],
                }
            )

    def test_create_music_tag_with_invalid_name(
        self, create_music_tag_valid_data, create_music_tag_invalid_data
    ):
        with pytest.raises(ValidationError):
            assert InsertMusicTagDto(
                **{
                    **create_music_tag_valid_data,
                    "name": create_music_tag_invalid_data["name"],
                }
            )

    def test_get_music_tag_with_valid_data(self, get_music_tag_valid_data):
        assert GetMusicTagDto(**get_music_tag_valid_data)

    def test_get_music_tag_with_invalid_user_id(
        self, get_music_tag_invalid_data, get_music_tag_valid_data
    ):
        with pytest.raises(ValidationError):
            assert GetMusicTagDto(
                **{
                    **get_music_tag_valid_data,
                    "user_id": get_music_tag_invalid_data["user_id"],
                }
            )

    def test_get_music_tag_with_invalid_name(
        self, get_music_tag_invalid_data, get_music_tag_valid_data
    ):
        with pytest.raises(ValidationError):
            assert GetMusicTagDto(
                **{
                    **get_music_tag_valid_data,
                    "name": get_music_tag_invalid_data["name"],
                }
            )

    def test_get_music_tag_without_id(
        self, get_music_tag_invalid_data, get_music_tag_valid_data
    ):
        get_music_tag_valid_data.pop("id")
        with pytest.raises(ValidationError):
            assert GetMusicTagDto(**get_music_tag_valid_data)


class TestMusicServices:
    def test_insert_music(self, create_valid_data):
        session = Mock()
        session.commit = MagicMock()

        music = Music(**create_valid_data)

        repo = Mock()
        repo.create = MagicMock(return_value=music)
        (session, create_valid_data, repo)

        result = music_services.insert_music(session, create_valid_data, repo)

        assert music.name == result.name

    def test_list_user_musics(self, create_valid_data):
        session = Mock()
        music = Music(**create_valid_data)
        user = User(
            id=1, name="Joao", email="joao@email.com", password="123456", musics=[music]
        )

        repo = Mock()

        repo.get_one = MagicMock(return_value=user)

        result = music_services.list_user_musics(session, user.id, repo)

        assert len(result) == 1
        result[0].name = music.name
        result[0].user_id = music.user_id
        result[0].artist = music.artist


class TestMusicTagServices:
    def test_create_music_tag_services(self, create_music_tag_valid_data):
        repo = Mock()
        session = Mock()
        session.commit = MagicMock()

        music_tag = MusicTag(**create_music_tag_valid_data, id=1)
        repo.create = MagicMock(return_value=music_tag)
        result = music_tag_services.create_music_tag(
            session, create_music_tag_valid_data, repo
        )

        assert result.id == 1

    def test_get_music_tag_services(self, get_music_tag_valid_data):
        repo = Mock()
        session = Mock()
        session.commit = MagicMock()

        music_tag = MusicTag(**get_music_tag_valid_data)
        repo.get = MagicMock(return_value=[music_tag])
        result = music_tag_services.get_music_tag(session, music_tag.user_id, repo)

        assert len(result) == 1
        assert result[0].id == music_tag.id
        assert result[0].name == music_tag.name
        assert result[0].user_id == music_tag.user_id

    def test_update_music_tag(self, get_music_tag_valid_data):
        repo = Mock()
        session = Mock()
        session.commit = MagicMock()

        music_tag = MusicTag(**get_music_tag_valid_data)
        repo.update_by_id = MagicMock(return_value=music_tag)
        result = music_tag_services.update_music_tag(
            session, get_music_tag_valid_data, repo
        )

        assert result.id == music_tag.id
        assert result.name == music_tag.name
        assert result.user_id == music_tag.user_id

    def test_delete_music_tag(self, get_music_tag_valid_data):
        repo = Mock()
        repo.delete_one = MagicMock()
        session = Mock()
        session.commit = Mock()

        result = music_tag_services.delete_music_tag(
            session, get_music_tag_valid_data, repo
        )

        assert result["id"] == get_music_tag_valid_data["id"]