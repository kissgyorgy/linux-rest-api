import os
import stat


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
