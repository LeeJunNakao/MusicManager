from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from config import get_settings

metadata = MetaData(
    naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }
)
database = SQLAlchemy(metadata=metadata)


def init_database() -> SQLAlchemy:
    import adapters.orm

    # settings = get_settings()
    # if settings.FLASK_ENV == "testing":
    #     metadata.create_all(engine)

    return database
