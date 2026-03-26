# service.py
from datastore import database  # assume database = {} is defined in datastore.py


def process_and_store(key, value):
    """
    Process the value (strip whitespace, convert to uppercase) 
    and store it. Return processed value (uppercase).
    """
    processed = value.strip().upper()
    database[key] = value.strip()  # store the cleaned but not uppercased version
    return processed


def retrieve_processed(key):
    """
    Retrieve the stored value in lowercase format.
    Return None if key does not exist.
    """
    value = database.get(key)
    if value is not None:
        return value.lower()
    return None


def update_value(key, new_value):
    """
    Update the stored value for a key.
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
    """Return a list of all keys."""
    return list(database.keys())
