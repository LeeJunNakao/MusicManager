from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE: str
    DATABASE_USERNAME: str
    DATABASE_PASSWORD: str
    DATABASE_HOST: str
    DATABASE_PORT: str
    DATABASE_NAME: str
    DATABASE_URI: str
    HASH_SALT: str
    JWT_SECRET: str
    SMTP_HOST: str
    SMTP_PORT: str
    SMTP_USER: str
    SMTP_PASSWORD: str


def get_settings():
    settings = Settings()
    settings.DATABASE_URI = f"{settings.DATABASE}://{settings.DATABASE_USERNAME}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_HOST}:{settings.DATABASE_PORT}/{settings.DATABASE_NAME}"

    return settings


database_uri = get_settings().DATABASE_URI

engine = create_engine(database_uri)
get_session = sessionmaker(bind=engine)
