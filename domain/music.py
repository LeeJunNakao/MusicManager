from dataclasses import dataclass
from pydantic import BaseModel, constr
from typing import Optional, List


@dataclass
class Music:
    id: int
    user_id: int
    name: str
    artist: str
    info: str


class InsertMusicDto(BaseModel):
    user_id: int
    name: constr(min_length=1, max_length=40)
    artist: constr(min_length=1, max_length=40)
    album: Optional[constr(min_length=1, max_length=40)]
    tag_id: Optional[int]
    info: Optional[constr(max_length=100)]


class GetMusicDto(BaseModel):
    id: int
    name: constr(min_length=1)
    artist: constr(min_length=1)
    info: Optional[str]
    album: Optional[str]
    tag_id: Optional[int]


@dataclass
class MusicTag(BaseModel):
    id: int
    user_id: int
    name: str


class InsertMusicTagDto(BaseModel):
    user_id: int
    name: constr(min_length=1, max_length=30)


class GetMusicTagDto(BaseModel):
    id: int
    user_id: int
    name: str
