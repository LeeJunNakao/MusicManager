from typing import Protocol
from .domain import IUser, IMusic, IMusic
from domain.music import Music


class UserRepository(Protocol):
    def create(self, session, data: dict) -> None:
        ...

    def update_by_id(self, dto):
        ...

    def list(self):
        ...

    def get_one(self, dto) -> IUser:
        ...


class MusicRepository(Protocol):
    def create(self, session, data: dict) -> None:
        ...

    def update_by_id(self, dto):
        ...

    def list(self):
        ...

    def get_one(self, dto) -> IMusic:
        ...
