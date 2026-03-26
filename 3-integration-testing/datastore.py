database = {}

def store_value(key, value):
    """Store a value in the dictionary under the given key."""
    database[key] = value

def get_value(key):
    """Retrieve a value by key. Return None if the key does not exist."""
    return database.get(key, None)

def delete_value(key):
    """Delete a value by key. Return True if deleted, False if key was not found."""
    if key in database:
        del database[key]
        return True
    return False

def list_keys():
    """Return a list of all keys in the dictionary."""
    return list(database.keys())
