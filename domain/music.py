from dataclasses import dataclass
from pydantic import BaseModel
from typing import Optional


class Music:
    name: str
    artist: str
    id: int
    info: str


class MusicDto(BaseModel):
    id: Optional[int]
    name: Optional[str]
    artist: Optional[str]
