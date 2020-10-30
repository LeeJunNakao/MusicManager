from typing import Any
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, MetaData, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import mapper, relationship
from adapters.orm.user import User


Base: Any = declarative_base()
music_metadata = Base.metadata


class Music(Base):
    __tablename__ = "music"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    name = Column(String, nullable=False)
    artist = Column(String, nullable=False)
    info = Column(String)
