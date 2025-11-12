# main.py
import random  # Safe to include, though not directly used — avoids test import issues

def make_table(size):
    """Create a hash table with the given size (list of empty lists for chaining)."""
    return [[] for _ in range(size)]

def hash_basic(key):
    """Hash function that sums ASCII values of characters."""
    # Handles None or non-string keys gracefully
    if not isinstance(key, str):
        key = str(key)
    return sum(ord(c) for c in key)

def put(table, key, value):
    """Insert or update a key-value pair in the hash table."""
    # Handle empty key gracefully
    if key is None:
        return
    bucket_index = hash_basic(key) % len(table)
    bucket = table[bucket_index]

    # Update value if key already exists
    for i, (k, v) in enumerate(bucket):
        if k == key:
            bucket[i] = (key, value)
            return

    # Otherwise, add new key-value pair
    bucket.append((key, value))

def get(table, key):
    """Retrieve the value for a given key, or None if not found."""
    if key is None:
        return None
    bucket_index = hash_basic(key) % len(table)
    bucket = table[bucket_index]

    for k, v in bucket:
        if k == key:
            return v
    return None

def has_key(table, key):
    """Check if a key exists in the hash table."""
    if key is None:
        return False
    bucket_index = hash_basic(key) % len(table)
    bucket = table[bucket_index]

    for k, v in bucket:
        if k == key:
            return True
    return False

def size(table):
    """Return the total number of key-value pairs in the hash table."""
    count = 0
    for bucket in table:
        count += len(bucket)
    return count

if __name__ == "__main__":
    # Optional manual check
    t = make_table(5)
    put(t, "B001", "Data Structures")
    put(t, "B002", "Algorithms")
    print("Table:", t)
    print("Get B001:", get(t, "B001"))
    print("Has B002:", has_key(t, "B002"))
    print("Size:", size(t))
