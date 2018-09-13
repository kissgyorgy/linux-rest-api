import stat


def octal_mode(st_mode: int) -> str:
    return oct(stat.S_IMODE(st_mode))[2:]


def symbolic_mode(st_mode: int) -> str:
    lm = long_mode(st_mode)
    user = lm[0:3].replace("-", "")
    group = lm[3:6].replace("-", "")
    other = lm[6:].replace("-", "")
    return f"u={user},g={group},o={other}"


def long_mode(st_mode: int) -> str:
    return stat.filemode(st_mode)[1:]
