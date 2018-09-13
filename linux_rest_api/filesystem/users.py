import pwd
import grp


def get_user(uid: int):
    try:
        return pwd.getpwuid(uid).pw_name
    except KeyError:
        return None


def get_group(gid: int) -> str:
    try:
        return grp.getgrgid(gid).gr_name
    except KeyError:
        return None
