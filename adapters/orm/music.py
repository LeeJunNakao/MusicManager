from typing import Any
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, MetaData, Column, Integer, String, Date
from sqlalchemy.orm import mapper, relationship

from domain.music import Music as MusicDomain

Base: Any = declarative_base()
music_metadata = Base.metadata


class Music(Base, MusicDomain):
    __tablename__ = "music"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    artist = Column(String)
    info = Column(String)
