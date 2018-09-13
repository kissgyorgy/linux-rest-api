from linux_rest_api import filesystem as fs


ST_MODE_FILE_644 = 0o100644
ST_MODE_DIRECTORY_755 = 0o40755


def test_octal_mode():
    assert fs.octal_mode(ST_MODE_FILE_644) == "644"
    assert fs.octal_mode(ST_MODE_DIRECTORY_755) == "755"


def test_symbolic_mode():
    assert fs.symbolic_mode(ST_MODE_FILE_644) == "u=rw,g=r,o=r"
    assert fs.symbolic_mode(ST_MODE_DIRECTORY_755) == "u=rwx,g=rx,o=rx"


def test_long_mode():
    assert fs.long_mode(ST_MODE_FILE_644) == "rw-r--r--"
    assert fs.long_mode(ST_MODE_DIRECTORY_755) == "rwxr-xr-x"
