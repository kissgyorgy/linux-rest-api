from flask import Blueprint, jsonify
from .dirs import list_dir


bp = Blueprint("dirs", __name__)


@bp.route("<fullpath:fullpath>", methods=["LIST"])
def list_dir_view(fullpath="/"):
    print("GOT fullpath:", fullpath, flush=True)
    return jsonify(list(list_dir(fullpath)))
