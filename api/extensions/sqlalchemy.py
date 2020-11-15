from adapters.database_config import database


def configure_sqlalchemy(app):
    database.init_app(app)
    return app
