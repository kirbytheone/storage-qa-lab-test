import hashlib
import pytest


@pytest.mark.test_id("STORAGE-TEST-004")
@pytest.mark.summary("Checksum validation after write")
def test_checksum(storage_path):
    file = storage_path / "checksum.bin"
    data = b"important data"

    file.write_bytes(data)

    expected = hashlib.sha256(data).hexdigest()
    actual = hashlib.sha256(file.read_bytes()).hexdigest()

    assert expected == actual

    file.unlink()
