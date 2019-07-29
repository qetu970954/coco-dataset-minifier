from fnmatch import fnmatch
from os import listdir
from pathlib import Path
from shutil import copyfile

import pytest


@pytest.fixture()
def setup_working_directory():
    # Create an environment in order to apply LineRemover
    Path("tests/resources/tmp").mkdir(parents=True, exist_ok=True)
    names = [name for name in listdir("tests/resources/") if fnmatch(name, '*.txt')]
    for name in names:
        copyfile(f"tests/resources/{name}", f"tests/resources/tmp/{name}")
