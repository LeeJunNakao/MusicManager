from flask import (
    Blueprint,
    request,
)
from flask import jsonify

from adapters.database_config import get_session
from services.music_tag_services import (
    create_music_tag,
    get_music_tag,
    update_music_tag,
    delete_music_tag,
)
from api.utils.decorators import login_required

bp = Blueprint("music_tag", __name__, url_prefix="/music_tag")


@bp.route("", methods=["POST", "GET"])
@login_required
def create_route():
    session = get_session()

    try:
        if request.method == "POST":
            music_tag = {**request.json, "user_id": request.user_info["id"]}
            music_tag = create_music_tag(session, music_tag)
        else:
            music_tag = get_music_tag(session, request.user_info["id"])

            return jsonify([tag.dict() for tag in music_tag]), 200
        return music_tag.dict(), 201

    except Exception:
        if request.method == "POST":
            return "Não foi possível criar tag", 400
        else:
            return "Não foi possível localizar tag", 400


@bp.route("/<int:id_>", methods=["PUT", "DELETE"])
@login_required
def music_tag_route(id_):
    session = get_session()

    try:
        if request.method == "PUT":
            music_tag = update_music_tag(
                session,
                {
                    **request.json,
                    "id": id_,
                    "user_id": request.user_info["id"],
                },
            )

            response = music_tag.dict()

        else:
            response = delete_music_tag(
                session,
                {
                    "id": id_,
                    "user_id": request.user_info["id"],
                },
            )
        return response, 200
    except Exception:
        if request.method == "PUT":
            return "Não foi possível atualizar tag", 400
        else:
            return "Não foi possível deletar tag", 400
