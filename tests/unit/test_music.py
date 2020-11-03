import pytest
from pydantic import ValidationError
from domain.music import InsertMusicDto, GetMusicDto


@pytest.fixture(name="create_valid_data")
def create_valid_data_fixture():
    return {
        "user_id": 7,
        "name": "Californication",
        "artist": "Red Hot Chilli Peppers",
        "info": "nice song",
    }


@pytest.fixture(name="create_invalid_data")
def crate_invalid_data_fixture():
    return {"user_id": "ten", "name": "", "artist": ""}


@pytest.fixture(name="get_valid_data")
def get_valid_data_fixture():
    return {
        "id": 255,
        "name": "Everlong",
        "artist": "Foo Fighters",
        "info": "The Colour and the Shape",
    }


@pytest.fixture(name="get_invalid_data")
def get_invalid_data_fixture():
    return {
        "id": None,
        "name": "",
        "artist": "",
    }


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
