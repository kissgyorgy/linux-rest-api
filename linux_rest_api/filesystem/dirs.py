import os
from pathlib import Path
from .types import file_type
from .modes import octal_mode, symbolic_mode, long_mode
from .users import get_user, get_group


def list_dir(path: Path):
    with os.scandir(path) as it:
        for entry in it:
            sr = entry.stat(follow_symlinks=False)
            yield {
                "name": entry.name,
                "type": file_type(entry, sr.st_mode),
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
