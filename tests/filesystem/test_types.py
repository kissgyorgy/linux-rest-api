import os
from linux_rest_api.filesystem import file_type
from .conftest import (
    make_test_file,
    make_test_dir,
    make_test_symlink,
    make_test_fifo,
    make_test_socket,
)


def make_st_modes_with_scandir(dir) -> dict:
    stats = {}
    with os.scandir(dir) as it:
        for entry in it:
            sr = entry.stat(follow_symlinks=False)
            stats[entry.name] = sr.st_mode
    return stats


def test_file_types(tmpdir):
    make_test_file(tmpdir, "regular_file")
    make_test_dir(tmpdir, "directory")
    make_test_symlink(tmpdir, "symlink", to="symlink")
    make_test_fifo(tmpdir, "fifo_file")
    make_test_socket(tmpdir, "socket")

    st_modes = make_st_modes_with_scandir(tmpdir)

    assert file_type(st_modes["regular_file"]) == "-"
    assert file_type(st_modes["directory"]) == "d"
    assert file_type(st_modes["fifo_file"]) == "p"
    assert file_type(st_modes["socket"]) == "s"
    assert file_type(st_modes["symlink"]) == "l"
