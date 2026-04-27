import pytest


@pytest.mark.test_id("STORAGE-TEST-006")
@pytest.mark.summary("Test multiple files creation")
def test_bulk_file_creation(storage_path):
    count = 10

    for i in range(count):
        file = storage_path / f"file_{i}.txt"
        file.write_text(f"data {i}")

    files = list(storage_path.glob("file_*.txt"))

    assert len(files) >= count

    for f in files:
        f.unlink()
