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
    def create(self):
        pass

    @classmethod
    @abc.abstractmethod
    def get(self):
        pass


class Repository(AbstractRepository):
    @classmethod
    def create(cls, session, data: dict):
        instance = cls.model(**data)
        session.add(instance)
        return instance

    @classmethod
    def get(cls, session, data):
        return session.query(cls.model).filter_by(**data).all()

    @classmethod
    def get_one(cls, session, data: dict):
        result = session.query(cls.model).filter_by(**data).one()
        return result

    @classmethod
    def list(cls, session):
        return session.query(cls.model).all()

    @classmethod
    def delete_one(cls, session, data):
        instance = cls.get_one(session, data)
        session.delete(instance)


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

    @classmethod
    def update_by_id(cls, session, data: dict):
        instance = cls.get_one(session, dict(id=data["id"], user_id=data["user_id"]))
        for key in data.keys():
            setattr(instance, key, data[key])
        return instance
