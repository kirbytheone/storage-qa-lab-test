import os
import pytest


@pytest.mark.test_id("STORAGE-TEST-007")
@pytest.mark.summary("Check write permissions")
def test_write_permission(storage_path):
    file = storage_path / "perm.txt"

    file.write_text("test")

    assert os.access(file, os.W_OK)

    file.unlink()
