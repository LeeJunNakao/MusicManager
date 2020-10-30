from flask import Flask, jsonify, request
from . import auth
from . import music


def create_app():
    app = Flask(__name__)

    app.register_blueprint(auth.bp)
    app.register_blueprint(music.bp)

    return app
