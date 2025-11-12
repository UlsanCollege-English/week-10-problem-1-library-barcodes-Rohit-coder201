 
import random

from main import make_table, hash_basic, put, get, has_key, size

# ---- Normal tests (4) ----

def test_make_table_and_empty_size():
    t = make_table(5)
    assert isinstance(t, list)
    assert len(t) == 5
    assert size(t) == 0

def test_put_and_get_basic():
    t = make_table(5)
    put(t, "B123", "Data Structures")
    assert get(t, "B123") == "Data Structures"
    assert get(t, "X999") is None

def test_overwrite_same_key():
    t = make_table(7)
    put(t, "C777", "Old")
    put(t, "C777", "New")
    assert get(t, "C777") == "New"
    assert size(t) == 1

def test_has_key_true_false():
    t = make_table(3)
    put(t, "L001", "Linear Algebra")
    assert has_key(t, "L001") is True
    assert has_key(t, "M123") is False

# ---- Edge-case tests (3) ----

def test_collision_same_bucket():
    t = make_table(2)  # force collisions
    # Craft two keys that likely collide under sum-of-ords % 2
    put(t, "AA", "T1")
    put(t, "BB", "T2")
    assert size(t) == 2
    assert set(v for _, v in t[0] + t[1]) == {"T1", "T2"}

def test_empty_string_key_not_allowed_but_handled_gracefully():
    t = make_table(5)
    # Behavior left to student; tests just ensure functions exist and do not crash on empty key use
    put(t, "", "EmptyTitle")
    # Should still be retrievable if stored
    assert get(t, "") in (None, "EmptyTitle")

def test_unicode_keys():
    t = make_table(5)
    put(t, "책123", "K-Book")
    assert has_key(t, "책123") is True
    assert get(t, "책123") == "K-Book"

# ---- More-complex tests (3) ----

def test_many_inserts_and_size_counts():
    t = make_table(11)
    for i in range(100):
        put(t, f"ID{i}", f"T{i}")
    assert size(t) == 100
    # spot check
    assert get(t, "ID0") == "T0"
    assert get(t, "ID99") == "T99"

def test_randomized_collisions_are_retrievable():
    t = make_table(5)
    keys = ["K" + str(i) for i in range(50)]
    for k in keys:
        put(t, k, k.lower())
    random.shuffle(keys)
    for k in keys:
        assert get(t, k) == k.lower()

def test_hash_basic_stability():
    s = "Barcode-XYZ"
    assert hash_basic(s) == hash_basic(s)
