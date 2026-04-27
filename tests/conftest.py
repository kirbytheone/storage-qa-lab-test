import os
from pathlib import Path

import pytest


@pytest.fixture
def storage_path() -> Path:
    path = Path(os.getenv("STORAGE_PATH", "/tmp/storage_qa_lab"))
    path.mkdir(parents=True, exist_ok=True)
    return path
