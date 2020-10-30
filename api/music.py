from flask import Blueprint, request
from services import music_services
from api.utils.decorators import login_required
from adapters.repository import UserRepository
import json

bp = Blueprint("music", __name__, url_prefix="/music")


@bp.route("", methods=["POST"])
@login_required
def music_route():
    try:
        music = music_services.insert_music(
            **{**dict(request.json), "user_id": request.user_info["id"]}
        )
        return music, 200
    except:
        return "Não foi possível cadastrar a musica", 400


@bp.route("", methods=["GET"])
def user_musics():
    try:
        musics = music_services.list_user_musics(request.json["user_id"])
        return json.dumps(musics), 200
    except:
        return "Não foi possível efetivar pesquisa.", 200
