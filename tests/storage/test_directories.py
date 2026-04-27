import pytest


@pytest.mark.test_id("STORAGE-TEST-005")
@pytest.mark.summary("Check Nested directories creation")
def test_nested_directories(storage_path):
    nested = storage_path / "a" / "b" / "c"

    nested.mkdir(parents=True, exist_ok=True)

    assert nested.exists()
    assert nested.is_dir()
