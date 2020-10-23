from flask import Flask, jsonify, request
import json
import config
from adapters.orm import Music
from adapters import orm, repository
from services import music_services

app = Flask(__name__)



@app.route("/music", methods=["POST"])
def music_route():
    session = config.get_session()
    repo = repository.MusicRepository(session)
    music = Music(**dict(request.json))

    try:
        music_services.insert_music(music, repo, session)

        return request.json, 200
    except:
        return "Não foi possível cadastrar a musica", 400
