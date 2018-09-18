import os
from pathlib import Path
from .files import get_attributes


def list_dir(path: Path):
    with os.scandir(path) as it:
        for entry in it:
            sr = entry.stat(follow_symlinks=False)
            yield get_attributes(entry.name, sr)
