# Storage QA Raspberry Pi 5 Automation


This project demonstrates automated storage validation testing using Python, pytest, Docker, Jenkins, 
and Raspberry Pi 5 infrastructure.
The framework validates file operations, data integrity, mounted storage behavior, permissions, 
and directory structures in a Linux-based environment.

## Project Structure

```text
storage-qa-lab-test/
├── tests/storage/
│   ├── test_bulk.py
│   ├── test_directories.py
│   ├── test_file_integrity.py
│   ├── test_mount.py
│   ├── test_permissions.py
│   └── test_simple_file_operations.py
├── local_storage/
├── Jenkinsfile
├── pytest.ini
├── requirements.txt
└── README.md
```
## STORAGE TESTS

- File operations testing (create, read, update, delete)
- Data integrity validation (checksums)
- Directory structure validation
- Bulk file operations
- Permission checks

## ARCHITECTURE

MacBook Pro → GitHub → Jenkins (Docker on Raspberry Pi 5) → Python test container → mounted storage validation

## Run locally

```bash
pytest -v
```

## STORAGE SETUP

Tests expect a mounted storage device.

Example:

```bash
sudo mount /dev/sda1 /mnt/storage_qa

## Run against real storage
STORAGE_PATH=/mnt/storage_qa pytest -v
```

## CI 
Tests are executed in Docker via Jenkins pipeline.