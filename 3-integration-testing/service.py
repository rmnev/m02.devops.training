# service.py
from datastore import database  # database = {} in datastore.py

def process_and_store(key, raw_value):
    """
    Process the value (strip whitespace, convert to uppercase for return)
    but store trimmed value as-is in the database.
    """
    processed = raw_value.strip().upper()
    database[key] = raw_value.strip()
    return processed

def retrieve_processed(key):
    """
    Retrieve the stored value. Return lowercase version if exists,
    None if the key does not exist.
    """
    value = database.get(key)
    return value.lower() if value is not None else None

def update_value(key, new_value):
    """
    Update a stored value for an existing key.
    """
    if key in database:
        database[key] = new_value.strip()
        return True
    return False

def delete_value(key):
    """
    Delete a key from the database.
    Return True if deleted, False if key not found.
    """
    if key in database:
        del database[key]
        return True
    return False

def list_all_keys():
    """
    Return a list of all keys currently in the database.
    """
    return list(database.keys())
