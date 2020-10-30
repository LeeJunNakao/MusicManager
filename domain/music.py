from dataclasses import dataclass
from pydantic import BaseModel, constr
from typing import Optional


@dataclass
class Music:
    name: str
    artist: str
    id: int
    info: str


class InsertMusicDto(BaseModel):
    user_id: int
    name: constr(min_length=1)
    artist: constr(min_length=1)
    info: Optional[str]
