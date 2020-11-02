import sys
from flask import (
    Blueprint,
    request,
)
import json
from services import auth_services
from api.utils.decorators import login_required

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/register", methods=["POST"])
def register_route():
    try:
        user = auth_services.create_user(**dict(request.json))
        return json.dumps(user), 200
    except:
        return "Não foi possível criar usuario", 400


@bp.route("/login", methods=["POST"])
def login_route():
    try:
        response = auth_services.login(**dict(request.json))
        return json.dumps(response), 200
    except:
        return "Acesso negado!", 400
