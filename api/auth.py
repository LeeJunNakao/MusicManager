from flask import (
    Blueprint,
    request,
)
import json
from adapters.database_config import get_session
from services import auth_services

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/register", methods=["POST"])
def register_route():
    session = get_session()
    try:
        user = auth_services.create_user(session, **dict(request.json))
        return user, 201
    except:
        return "Não foi possível criar usuario", 400


@bp.route("/login", methods=["POST"])
def login_route():
    session = get_session()
    try:
        response = auth_services.login(session, **dict(request.json))
        return response, 200
    except:
        return "Acesso negado!", 400
