from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE: str
    DATABASE_USERNAME: str
    DATABASE_PASSWORD: str
    DATABASE_HOST: str
    DATABASE_PORT: str
    DATABASE_NAME: str
    SQLALCHEMY_DATABASE_URI: str
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    HASH_SALT: str
    JWT_SECRET: str
    SMTP_HOST: str
    SMTP_PORT: str
    SMTP_USER: str
    SMTP_PASSWORD: str
    FLASK_ENV: str


def get_settings():
    settings = Settings()
    settings.SQLALCHEMY_DATABASE_URI = f"{settings.DATABASE}://{settings.DATABASE_USERNAME}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_HOST}:{settings.DATABASE_PORT}/{settings.DATABASE_NAME}"
    return settings


def configure_environment(app, settings):
    app.config.from_object(settings)
    return app
