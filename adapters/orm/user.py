from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from adapters.database_config import database


class User(database.Model):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(256), nullable=False)
    musics = relationship("Music", back_populates="user")
