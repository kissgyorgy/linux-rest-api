import os
import stat


def file_type(entry: os.DirEntry, st_mode: int):
    if entry.is_file(follow_symlinks=False):
        return "-"
    elif entry.is_dir(follow_symlinks=False):
        return "d"
    elif entry.is_symlink():
        return "l"
    elif stat.S_ISSOCK(st_mode):
        return "s"
    elif stat.S_ISCHR(st_mode):
        return "c"
    elif stat.S_ISBLK(st_mode):
        return "b"
    elif stat.S_ISFIFO(st_mode):
        return "p"
