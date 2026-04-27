import pytest


class TestSimpleFileOperations:

    @pytest.mark.test_id("STORAGE-TEST-002")
    @pytest.mark.summary("Create and read file")
    def test_create_and_read(self, storage_path):
        file = storage_path / "test.txt"

        file.write_text("hello")
        assert file.read_text() == "hello"

        file.unlink()

    @pytest.mark.test_id("STORAGE-TEST-003")
    @pytest.mark.summary("Update file content")
    def test_update_file(self, storage_path):
        file = storage_path / "update.txt"

        file.write_text("old")
        file.write_text("new")

        assert file.read_text() == "new"
        file.unlink()
