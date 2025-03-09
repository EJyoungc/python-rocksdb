
import pytest
import rocksdb

def test_db_creation(tmp_path):
    db = rocksdb.DB(str(tmp_path / "test.db"), rocksdb.Options(create_if_missing=True))
    assert db is not None
