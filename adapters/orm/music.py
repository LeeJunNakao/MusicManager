from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from adapters.database_config import database
from adapters.orm.user import User


class Music(database.Model):
    __tablename__ = "music"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey(User.id, ondelete="CASCADE"), nullable=False)
    name = Column(String, nullable=False)
    artist = Column(String, nullable=False)
    info = Column(String)
    user = relationship("User", back_populates="musics")
