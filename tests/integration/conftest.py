import pytest
import os

from api import create_app
from adapters.database_config import init_database
from config import get_settings


@pytest.fixture(autouse=True)
def app():
    settings = get_settings()
    app = create_app()
    app.config["TESTING"] = "True"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = settings.DATABASE_URI
    
    return app


@pytest.fixture(autouse=True)
def truncate_tables(app):
    database = init_database()
    database.init_app(app)
    with app.app_context():
        with database.get_engine().connect() as conn:
            with conn.begin():
                tables_names = ",".join(
                    f"{table.name}" for table in database.metadata.sorted_tables
                )
                conn.execute("TRUNCATE {} RESTART IDENTITY".format(tables_names))
