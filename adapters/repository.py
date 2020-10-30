import abc
from dataclasses import dataclass
from adapters.orm.music import Music
from adapters.orm.user import User
import config


class AbstractRepository(abc.ABC):
    @classmethod
    @abc.abstractmethod
    def model():
        pass

    @property
    @classmethod
    @abc.abstractmethod
    def session():
        pass

    @classmethod
    @abc.abstractmethod
    def create(self, dto):
        pass

    @classmethod
    @abc.abstractmethod
    def get(self, dto):
        pass


class Repository(AbstractRepository):
    session = config.get_session()

    @classmethod
    def create(cls, **data):
        cls.session.add(cls.model(**data))
        cls.session.commit()

    @classmethod
    def get(cls, **data):
        return cls.session.query(cls.model).filter_by(**data).all()

    @classmethod
    def list(cls):
        return cls.session.query(cls.model).all()


class MusicRepository(Repository):
    model = Music


class UserRepository(Repository):
    model = User
    
    @classmethod
    def get_one(cls, **data):
        return cls.session.query(cls.model).filter_by(**data).one()
