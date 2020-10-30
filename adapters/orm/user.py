from typing import Any
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, MetaData, Column, Integer, String, Date
from sqlalchemy.orm import mapper, relationship

from domain.user import User as UserDomain

Base: Any = declarative_base()
user_metadata = Base.metadata


class User(Base, UserDomain):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(256), nullable=False)

