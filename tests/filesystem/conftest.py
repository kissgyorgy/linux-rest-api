import os
import socket
from pathlib import Path
import pytest
from linux_rest_api import filesystem as fs


def make_test_file(dir: Path, filename: str, content=None):
    test_file = dir / filename
    test_file.touch()
    if content is not None:
        test_file.write_bytes(content)


def make_test_dir(dir: Path, dirname: str):
    (dir / dirname).mkdir()


def make_test_symlink(dir: Path, filename: str, to: str):
    (dir / filename).symlink_to(to)


def make_test_fifo(dir: Path, filename: str):
    os.mkfifo(dir / filename)


def make_test_socket(dir: Path, filename: str):
    # A socket filename cannot be too long: https://github.com/ethereum/web3.py/issues/929
    # this is a workaround, so we don't have to use the full path
    os.chdir(dir)
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.bind(filename)


@pytest.fixture(scope="session")
def make_file_attributes():
    current_uid = os.getuid()
    current_gid = os.getgid()

    def make_filetype_dict(name, mode, symbolic_mode, long_mode, ftype, size):
        return {
            "name": name,
            "uid": current_uid,
            "gid": current_gid,
            "user": fs.get_user(current_uid),
            "group": fs.get_group(current_gid),
            "mode": mode,
            "mode_symbolic": symbolic_mode,
            "mode_long": long_mode,
            "type": ftype,
            "size": size,
        }

    return make_filetype_dict
