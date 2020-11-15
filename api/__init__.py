from flask import Flask
from . import auth
from . import music
from . import music_tag
from api.extensions.sqlalchemy import configure_sqlalchemy
from config import get_settings, configure_environment


def create_app():
    app = Flask(__name__)
    settings = get_settings()
    app = configure_environment(app, settings)
    app = configure_sqlalchemy(app)
    app.register_blueprint(auth.bp)
    app.register_blueprint(music.bp)
    app.register_blueprint(music_tag.bp)
    
    return app
