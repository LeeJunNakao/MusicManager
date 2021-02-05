import json

from flask import Blueprint, request
from services import music_services
from api.utils.decorators import login_required
from adapters.database_config import get_session
from adapters.repository import MusicRepository, UserRepository
from pydantic import ValidationError
from services.utils.exceptions import CustomValidationError

bp = Blueprint("music", __name__, url_prefix="/music")


@bp.route("", methods=["POST"])
@login_required
def music_route():
    session = get_session()
    try:
        music = music_services.insert_music(
            session,
            {**dict(request.json), "user_id": request.user_info["id"]},
            MusicRepository,
        )
        return music.dict(), 200
    except ValidationError as e:
        error = CustomValidationError(e)
        return error.message, 400
    except Exception as error:
        return error.message, 400


@bp.route("", methods=["GET"])
@login_required
def user_musics():
    try:
        session = get_session()
        musics = music_services.list_user_musics(
            session, request.user_info["id"], UserRepository
        )
        return json.dumps(musics), 200
    except:
        return "Não foi possível efetivar pesquisa.", 200
