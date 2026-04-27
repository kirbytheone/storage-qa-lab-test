import pytest


@pytest.mark.test_id("STORAGE-TEST-001")
@pytest.mark.summary("Storage path and its directory exists")
def test_storage_available(storage_path):
    assert storage_path.exists()
    assert storage_path.is_dir()
