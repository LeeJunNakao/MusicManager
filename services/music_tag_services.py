from domain.music import InsertMusicTagDto, GetMusicTagDto
from adapters.repository import MusicTagRepository


def create_music_tag(session, music_tag):

    dto = InsertMusicTagDto(**music_tag)

    try:
        music_tag = MusicTagRepository.create(session, dto.dict())
        session.commit()
        return GetMusicTagDto(
            id=music_tag.id, user_id=music_tag.user_id, name=music_tag.name
        )
    except Exception:
        session.rollback()
        raise Exception
    finally:
        session.close()


def get_music_tag(session, user_id: int):

    try:
        music_tags = MusicTagRepository.get(session, dict(user_id=user_id))
        return [
            GetMusicTagDto(id=tag.id, user_id=tag.user_id, name=tag.user_name)
            for tag in music_tags
        ]
        session.commit()
    except Exception:
        session.rollback()
        raise Exception
    finally:
        session.close()
