import pytest
from pydantic import ValidationError
from domain.music import InsertMusicDto, GetMusicDto, InsertMusicTagDto, GetMusicTagDto


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
