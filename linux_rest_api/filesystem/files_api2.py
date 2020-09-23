import os
from pathlib import PurePath
from flask import Blueprint, jsonify, send_file
from .files import get_attributes


bp = Blueprint("files", __name__)


@bp.route("/<path:fullpath>", methods=["HEAD"])
def head_file(fullpath):
    return send_file("/" + fullpath)


@bp.route("/<path:fullpath>", methods=["LIST"])
def list_file(fullpath):
    name = PurePath(fullpath).name
    sr = os.stat("/" + fullpath, follow_symlinks=False)
    return jsonify(get_attributes(name, sr))


@bp.route("/<path:fullpath>", methods=["TAIL"])
def tail_file(fullpath):
    """Sending the tail of the file, like the tail command,
    optionally following with follow=true HTTP param.
    """
    return send_file("/" + fullpath)


@bp.route("/<path:fullpath>", methods=["PUT"])
def upload_file(fullpath):
    return request.files


@bp.route("/<path:fullpath>", methods=["PATCH"])
def patch_file(fullpath):
    """This is ACTUALLY expecting a unified diff and patching the file."""
    return request.files
