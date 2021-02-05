from domain.music import InsertMusicDto, Music
from domain.user import User
from typing import List
from protocols.repository import MusicRepository
from services.utils.exceptions import PersistenceError

def insert_music(session, music: dict, music_repo: MusicRepository) -> Music:

    dto = InsertMusicDto(**music)
    data = dto.dict()

    try:
        result = music_repo.create(session, data)
        session.commit()
        music_dto = Music.from_orm(result)
        return music_dto
    except Exception:
        session.rollback()
        raise PersistenceError
    finally:
        session.close()


def list_user_musics(session, user_id: int, user_repo) -> List[Music]:

    user = user_repo.get_one(session, dict(id=user_id))
    user_dto = User.from_orm(user)

    return user_dto.musics
