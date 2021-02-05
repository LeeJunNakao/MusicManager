from typing import Protocol, List


class IMusicTag(Protocol):
    id: int
    user_id: int
    name: str


class IMusic(Protocol):
    id: int
    user_id: int
    name: str
    artist: str
    info: str


class IUser(Protocol):
    id: int
    name: str
    email: str
    password: str
    musics: List[IMusic]
