from .metadata import Base
from sqlalchemy import Table, MetaData, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import mapper, relationship
from adapters.orm.user import User


music_metadata = Base.metadata


class Music(Base):
    __tablename__ = "music"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey(User.id, ondelete="CASCADE"), nullable=False)
    name = Column(String, nullable=False)
    artist = Column(String, nullable=False)
    info = Column(String)
    user = relationship("User", back_populates="musics")
