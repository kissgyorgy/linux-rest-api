from linux_rest_api.filesystem import file_type
from .conftest import (
    make_test_file,
    make_test_dir,
    make_test_symlink,
    make_test_fifo,
    make_test_socket,
    make_entires_with_scandir,
)


def test_file_types(tmpdir):
    make_test_file(tmpdir, "regular_file")
    make_test_dir(tmpdir, "directory")
    make_test_symlink(tmpdir, "symlink", to="symlink")
    make_test_fifo(tmpdir, "fifo_file")
    make_test_socket(tmpdir, "socket")

    entries = make_entires_with_scandir(tmpdir)

    assert file_type(*entries["regular_file"]) == "-"
    assert file_type(*entries["directory"]) == "d"
    assert file_type(*entries["fifo_file"]) == "p"
    assert file_type(*entries["socket"]) == "s"
    assert file_type(*entries["symlink"]) == "l"
