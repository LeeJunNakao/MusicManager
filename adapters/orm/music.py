from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from adapters.database_config import database
from adapters.orm.user import User


class MusicTag(database.Model):
    __tablename__ = "music_tag"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey(User.id, ondelete="CASCADE"), nullable=False)
    name = Column(String)
    musics = relationship("Music", back_populates="tag")


class Music(database.Model):
    __tablename__ = "music"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey(User.id, ondelete="CASCADE"), nullable=False)
    name = Column(String, nullable=False)
    artist = Column(String, nullable=False)
    info = Column(String)
    album = Column(String)
    tag_id = Column(Integer, ForeignKey(MusicTag.id, ondelete="CASCADE"))
    user = relationship("User", back_populates="musics")
    tag = relationship("MusicTag", back_populates="musics")
