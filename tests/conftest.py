from pathlib import Path
import pytest


@pytest.fixture
def datadir(request):
    return Path(request.module.__file__).parent / "data"


@pytest.fixture
def tmpdir(tmpdir):
    return Path(tmpdir)
