from domain.music import Music
from adapters.repository import AbstractMusicRepository


def insert_music(music: Music, repo: AbstractMusicRepository, session):
    repo.create(music)

    session.commit()

    return music
