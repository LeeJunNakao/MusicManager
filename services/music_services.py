from domain.music import InsertMusicDto, GetMusicDto
from adapters.repository import MusicRepository, UserRepository


def insert_music(session, music: dict):

    dto = InsertMusicDto(**music)

    try:
        MusicRepository.create(session, **dto.dict())
        session.commit()
        return dto.dict()
    except Exception:
        session.rollback()
        raise Exception
    finally:
        session.close()


def list_user_musics(session, user_id: int):

    user = UserRepository.get_one(session, id=user_id)
    user_musics = user.musics
    musics = [GetMusicDto(**vars(music)).dict() for music in user_musics]

    return musics
