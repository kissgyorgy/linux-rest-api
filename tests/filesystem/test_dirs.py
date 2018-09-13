import os
import sys
from operator import itemgetter
import pytest
from linux_rest_api import filesystem as fs
from .conftest import (
    make_test_file,
    make_test_dir,
    make_test_fifo,
    make_test_socket,
    make_test_symlink,
)


@pytest.mark.skipif(
    sys.platform != "linux", reason="Sizes are different on other platforms"
)
def test_list_dir(tmpdir):
    make_test_file(tmpdir, "regular_file1", content=b"thirteenbytes")
    make_test_file(tmpdir, "regular_file2", content=b"four")
    make_test_dir(tmpdir, "directory")
    make_test_symlink(tmpdir, "symlink", to="doesntmatter")
    make_test_fifo(tmpdir, "fifo_file")
    make_test_socket(tmpdir, "socket")

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

    sorted_file_list = sorted(fs.list_dir(tmpdir), key=itemgetter("name"))

    expected_file_list = [
        make_filetype_dict(*attribs)
        for attribs in (
            ("directory", "755", "u=rwx,g=rx,o=rx", "rwxr-xr-x", "d", 4096),
            ("fifo_file", "644", "u=rw,g=r,o=r", "rw-r--r--", "p", 0),
            ("regular_file1", "644", "u=rw,g=r,o=r", "rw-r--r--", "-", 13),
            ("regular_file2", "644", "u=rw,g=r,o=r", "rw-r--r--", "-", 4),
            ("socket", "755", "u=rwx,g=rx,o=rx", "rwxr-xr-x", "s", 0),
            ("symlink", "777", "u=rwx,g=rwx,o=rwx", "rwxrwxrwx", "l", 12),
        )
    ]

    assert sorted_file_list == expected_file_list
