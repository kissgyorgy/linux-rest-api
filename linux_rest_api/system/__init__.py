import datetime as dt
from flask import Blueprint, jsonify
import psutil
from .os_release import get_os_release
from .uptime import iso8601now, get_uptime, get_load

bp = Blueprint("system", __name__)


@bp.route("/os-release", methods=["GET"])
def os_release():
    return jsonify(get_os_release())


@bp.route("/uptime", methods=["GET"])
def uptime():
    uptime_seconds, uptime_iso8601 = get_uptime()
    return jsonify(
        {
            "time": iso8601now(),
            "uptime": uptime_iso8601,
            "uptime_seconds": uptime_seconds,
            "users": len(psutil.users()),
            "load": get_load(),
        }
    )
