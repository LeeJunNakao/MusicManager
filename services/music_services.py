from domain.music import InsertMusicDto, GetMusicDto
from adapters.repository import MusicRepository, UserRepository


def insert_music(**music: dict):

    dto = InsertMusicDto(**music)
    MusicRepository.create(**dto.dict())

    return dto.dict()


def list_user_musics(user_id: int):

    user = UserRepository.get_one(id=user_id)
    user_musics = user.musics
    musics = [GetMusicDto(**vars(music)).dict() for music in user_musics]

    return musics
