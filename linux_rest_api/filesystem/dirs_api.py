from flask import Blueprint, jsonify
from .dirs import list_dir


bp = Blueprint("dirs", __name__)


# TODO: simplify this with an URL converter
@bp.route("/", methods=["LIST"])
@bp.route("/<path:fullpath>", methods=["LIST"])
def list_dir_view(fullpath=""):
    return jsonify(list(list_dir("/" + fullpath)))
