import pytest
from contextlib import contextmanager


from api import create_app
from adapters.database_config import init_database, database, get_session
from services import auth_services

@pytest.fixture(autouse=True)
def app():
    app = create_app()

    return app


def truncate_database() -> None:
    with database.get_engine().connect() as conn:
        with conn.begin():
            conn.execute(
                """TRUNCATE {} RESTART IDENTITY""".format(
                    ",".join(
                        f'"{table.name}"'
                        for table in reversed(database.metadata.sorted_tables)
                    )
                )
            )


@contextmanager
def clear_database():
    db = init_database()
    truncate_database()
    yield db


@pytest.fixture(autouse=True)
def exec_database(app):
    with app.app_context():
        with clear_database() as db:
            yield db


@pytest.fixture(name="user_info")
def get_valid_user_fixture():
    user_data = {
        "name": "João",
        "email": "joao@email.com",
        "password": "Abc123@",
    }
    session = get_session()
    jwt = auth_services.create_user(session, **user_data)
    user_info = auth_services.validate_token(jwt["token"])

    return user_info