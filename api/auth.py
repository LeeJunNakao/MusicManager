from flask import (
    Blueprint,
    request,
)
from adapters.database_config import get_session
from adapters.repository import UserRepository
from services import auth_services
from pydantic import ValidationError
from api.utils import exceptions

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/register", methods=["POST"])
def register_route():
    session = get_session()
    try:
        user = auth_services.create_user(session, dict(request.json), UserRepository)
        return user, 201
    except ValidationError:
        return exceptions.auth_validation_error, 400
    except Exception as error:
        return error.message, 400


@bp.route("/login", methods=["POST"])
def login_route():
    session = get_session()
    try:
        response = auth_services.login(session, dict(request.json), UserRepository)
        return response, 200
    except ValidationError:
        return exceptions.auth_validation_error, 400
    except Exception as error:
        return error.message, 400


@bp.route("/validate-token", methods=["POST"])
def validate_token():
    try:
        token = request.json["token"]
        decoded_token = auth_services.validate_token(token)
        response = {"token_validation": True, "user_id": decoded_token["id"]}
        return response, 200
    except Exception:
        return {"token_validation": False}, 401
