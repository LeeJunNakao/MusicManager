from domain.music import GetMusicTagDto, UpdateMusicTagDto, MusicTag, InsertMusicTagDto
from adapters.repository import MusicTagRepository


def create_music_tag(session, data, repo: MusicTagRepository) -> MusicTag:
    InsertMusicTagDto(**data)
    try:
        result = repo.create(session, data)
        session.commit()
        music_tag = MusicTag.from_orm(result)
        return music_tag
    except Exception as erro:
        session.rollback()
        raise Exception
    finally:
        session.close()


def get_music_tag(session, user_id: int, repo: MusicTagRepository):

    try:
        music_tags = repo.get(session, dict(user_id=user_id))
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


def update_music_tag(session, music_tag, repo: MusicTagRepository):

    dto = UpdateMusicTagDto(**music_tag)

    try:
        result = repo.update_by_id(session, dto.dict())
        music_tag = MusicTag.from_orm(result)
        session.commit()
        return music_tag
    except Exception:
        session.rollback()
        raise Exception
    finally:
        session.close()


def delete_music_tag(session, data, repo):
    try:
        repo.delete_one(session, data)
        session.commit()
        return {"id": data["id"]}
    except Exception:
        session.rollback()
        raise Exception
    finally:
        session.close()
