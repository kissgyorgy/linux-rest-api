import os
import stat
from .modes import octal_mode, symbolic_mode, long_mode
from .users import get_user, get_group


def file_type(st_mode: int):
    if stat.S_ISREG(st_mode):
        return "-"
    elif stat.S_ISDIR(st_mode):
        return "d"
    elif stat.S_ISLNK(st_mode):
        return "l"
    elif stat.S_ISSOCK(st_mode):
        return "s"
    elif stat.S_ISCHR(st_mode):
        return "c"
    elif stat.S_ISBLK(st_mode):
        return "b"
    elif stat.S_ISFIFO(st_mode):
        return "p"


def get_attributes(name: str, sr: os.stat_result) -> dict:
    return {
        "name": name,
        "type": file_type(sr.st_mode),
        "mode": octal_mode(sr.st_mode),
        "mode_symbolic": symbolic_mode(sr.st_mode),
        "mode_long": long_mode(sr.st_mode),
        "uid": sr.st_uid,
        # TODO: measure these and speed them up
        # (e.g. do it only once per function call)
        "user": get_user(sr.st_uid),
        "gid": sr.st_gid,
        "group": get_group(sr.st_gid),
        "size": sr.st_size,
    }
