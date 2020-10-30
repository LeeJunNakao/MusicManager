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
    except Exception as e:
        print(e)
        return "Não foi possível criar usuario", 400


@bp.route("/login", methods=["POST"])
def login_route():
    try:
        response = auth_services.login(**dict(request.json))
        return json.dumps(response), 200
    except:
        return "Acesso negado!", 400


@bp.route("/users", methods=["GET"])
def users():
    users = auth_services.list_users()

    users_list = [dict(user.__dict__) for user in users]
    [user.pop("password") for user in users_list]
    [user.pop("_sa_instance_state") for user in users_list]

    return json.dumps(users_list), 200
