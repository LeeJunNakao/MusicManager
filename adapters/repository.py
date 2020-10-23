import abc
from domain.music import Music, MusicDto


class AbstractMusicRepository(abc.ABC):
    @abc.abstractclassmethod
    def create(self, music: Music):
        pass

    def get(self, musicDto: MusicDto):
        pass


class MusicRepository(AbstractMusicRepository):
    def __init__(self, session):
        self.session = session

    def create(self, music: Music):
        self.session.add(music)

    def get(self, musicDto: MusicDto):
        return self.session.query(Music).filter_by(**dict(musicDto)).all()

    def list(self):
        return self.session.query(Music).all()
