from domain.music import InsertMusicDto, GetMusicDto
from adapters.repository import MusicRepository, UserRepository


def insert_music(session, music: dict):

    dto = InsertMusicDto(**music)

    try:
        music = MusicRepository.create(session, dto.dict())
        session.commit()
        return GetMusicDto(
            id=music.id,
            name=music.name,
            artist=music.artist,
            info=music.info,
            album=music.album,
            tag_id=music.tag_id,
        ).dict()
    except Exception:
        session.rollback()
        raise Exception
    finally:
        session.close()


def list_user_musics(session, user_id: int):

    user = UserRepository.get_one(session, dict(id=user_id))
    user_musics = user.musics
    musics = [GetMusicDto(**vars(music)).dict() for music in user_musics]

    return musics
