import os
from pathlib import PurePath
from flask import Blueprint, jsonify, send_file
from .files import get_attributes


bp = Blueprint("files", __name__)


@bp.route("/<path:fullpath>", methods=["LIST"])
def list_file(fullpath):
    name = PurePath(fullpath).name
    sr = os.stat("/" + fullpath, follow_symlinks=False)
    return jsonify(get_attributes(name, sr))


@bp.route("/<path:fullpath>", methods=["GET"])
def download_file(fullpath):
    return send_file("/" + fullpath)
