# STORAGE QA RUSPBERRY PI5 AUTOMATION

This project demonstrates automated storage testing using Python, pytest, Docker, and Jenkins.

## STORAGE TESTS

- File operations testing (create, read, update, delete)
- Data integrity validation (checksums)
- Directory structure validation
- Bulk file operations
- Permission checks

## ARCHITECTURE

Mac → GitHub → Jenkins (Docker on Raspberry Pi) → Python container → mounted storage

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