from flask import Blueprint, request
from services import music_services
from api.utils.decorators import login_required

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