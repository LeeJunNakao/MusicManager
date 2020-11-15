from domain.music import InsertMusicTagDto, GetMusicTagDto, UpdateMusicTagDto
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
        session.commit()
    
        return [
            GetMusicTagDto(id=tag.id, user_id=tag.user_id, name=tag.name)
            for tag in music_tags
        ]
    except Exception:
        session.rollback()
        raise Exception
    finally:
        session.close()


def update_music_tag(session, music_tag):

    dto = UpdateMusicTagDto(**music_tag)

    try:
        music_tag = MusicTagRepository.update_by_id(session, dto.dict())
        session.commit()
        return GetMusicTagDto(
            id=music_tag.id,
            user_id=music_tag.user_id,
            name=music_tag.name,
        )
    except Exception:
        session.rollback()
        raise Exception
    finally:
        session.close()


def delete_music_tag(session, data):
    try:
        MusicTagRepository.delete_one(session, data)
        session.commit()
        return {"id": data["id"]}
    except Exception:
        session.rollback()
        raise Exception
    finally:
        session.close()
