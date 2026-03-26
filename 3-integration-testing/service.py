import pytest
from service import store_value, get_value, delete_value, list_keys, database

def setup_function():
    # Reset the database before each test
    database.clear()

def test_store_and_get_value():
    store_value("name", "Alice")
    assert get_value("name") == "Alice"
    assert get_value("nonexistent") is None

def test_delete_value():
    store_value("age", 30)
    assert delete_value("age") is True
    # Deleting again should return False
    assert delete_value("age") is False

def test_list_keys():
    store_value("x", 1)
    store_value("y", 2)
    keys = list_keys()
    assert "x" in keys and "y" in keys
    assert len(keys) == 2
