from dataclasses import dataclass
from pydantic import BaseModel, constr
from typing import Optional


@dataclass
class Music:
    id: int
    name: str
    artist: str
    info: str


class InsertMusicDto(BaseModel):
    user_id: int
    name: constr(min_length=1)
    artist: constr(min_length=1)
    info: Optional[str]


class GetMusicDto(BaseModel):
    id: int
    name: constr(min_length=1)
    artist: constr(min_length=1)
    info: Optional[str]
