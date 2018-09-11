import platform
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


@bp.route("/uname", methods=["GET"])
def uname():
    uname = platform.uname()
    return jsonify(
        {
            # It's impossible to get an exact match for "uname -o" without calling
            # the uname binary itself, because there are distros like Tiny Core Linux
            # where the variable it's coming from is configurable. It's mostly
            # "GNU/Linux", but there are some exceptions where it's simply "Linux"
            # and faking "GNU/Linux here would be inaccurate sometimes.
            # See: https://git.busybox.net/busybox/commit/?id=64ed5f0d3c5eefbb208d4a334654834c78be2cbd
            # The response keys are coming from the uname(1) man page
            "kernel_name": uname.system,
            "nodename": uname.node,
            "kernel_release": uname.release,
            "kernel_version": uname.version,
            "machine": uname.machine,
            "processor": uname.processor or None,
        }
    )


@bp.route("/memory", methods=["GET"])
def memory():
    swapmem = psutil.swap_memory()
    return jsonify(
        {
            "memory": psutil.virtual_memory()._asdict(),
            "swap": {
                "total": swapmem.total,
                "used": swapmem.used,
                "free": swapmem.free,
                "percent": swapmem.percent,
                # sin and sout are terribly named IMO, so make them better
                "swap_in": swapmem.sin,
                "swap_out": swapmem.sout,
            },
        }
    )
