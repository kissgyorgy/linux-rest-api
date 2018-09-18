import os
from pathlib import Path
import pytest
from linux_rest_api import filesystem as fs
from .conftest import (
    make_test_file,
    make_test_dir,
    make_test_symlink,
    make_test_fifo,
    make_test_socket,
)


@pytest.fixture(scope="module")
def testdir(tmpdir_factory):
    tempdir = Path(tmpdir_factory.mktemp("test_files"))
    make_test_file(tempdir, "regular_file")
    make_test_dir(tempdir, "directory")
    make_test_symlink(tempdir, "symlink", to="symlink2")
    make_test_fifo(tempdir, "fifo_file")
    make_test_socket(tempdir, "socket")
    yield tempdir


# it is needed, because this way scandir() is only called once for every tests
@pytest.fixture(scope="module")
def statresults(testdir):
    stats = {}
    with os.scandir(testdir) as it:
        for entry in it:
            sr = entry.stat(follow_symlinks=False)
            stats[entry.name] = sr
        yield stats


@pytest.mark.parametrize(
    "filename,expected_type",
    [
        ("regular_file", "-"),
        ("directory", "d"),
        ("fifo_file", "p"),
        ("socket", "s"),
        ("symlink", "l"),
    ],
)
def test_file_types(testdir, statresults, filename, expected_type):
    assert fs.file_type(statresults[filename].st_mode) == expected_type


@pytest.mark.parametrize(
    "filename,stats",
    [
        ("regular_file", ("644", "u=rw,g=r,o=r", "rw-r--r--", "-", 0)),
        ("directory", ("755", "u=rwx,g=rx,o=rx", "rwxr-xr-x", "d", 4096)),
        ("fifo_file", ("644", "u=rw,g=r,o=r", "rw-r--r--", "p", 0)),
        ("socket", ("755", "u=rwx,g=rx,o=rx", "rwxr-xr-x", "s", 0)),
        ("symlink", ("777", "u=rwx,g=rwx,o=rwx", "rwxrwxrwx", "l", len("symlink2"))),
    ],
)
def test_file_attributes(testdir, statresults, make_file_attributes, filename, stats):
    attributes = fs.get_attributes(filename, statresults[filename])
    expected_attributes = make_file_attributes(filename, *stats)
    assert attributes == expected_attributes
