import abc
from adapters.orm.music import Music
from adapters.orm.user import User
from adapters.orm.music import MusicTag


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
    @classmethod
    def create(cls, session, data):
        instance = cls.model(**data)
        session.add(instance)
        return instance

    @classmethod
    def get(cls, session, **data):
        return session.query(cls.model).filter_by(**data).all()

    @classmethod
    def get_one(cls, session, data):
        return session.query(cls.model).filter_by(**data).one()

    @classmethod
    def list(cls, session):
        return session.query(cls.model).all()


class MusicRepository(Repository):
    model = Music


class UserRepository(Repository):
    model = User

    @classmethod
    def update_by_id(cls, session, data):
        instance = cls.get_one(session, dict(id=data["id"]))
        for key in data.keys():
            setattr(instance, key, data[key])


class MusicTagRepository(Repository):
    model = MusicTag
