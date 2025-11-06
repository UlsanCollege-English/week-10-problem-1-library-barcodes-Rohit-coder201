[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/VwTUWDlu)
# HW01 — Library Barcodes → Book Titles (Chaining)

**Story intro (new theme):**  
You volunteer at a **small campus library**. Each book has a **barcode**. You need a fast way to look up a **book title** from its barcode without scanning a long list.

**Today’s topic focus:** **Hash tables with chaining**.

---

## Technical description
- **Goal:** Implement a tiny hash table using **chaining** (a list of buckets; each bucket stores `[key, value]` pairs).
- **Functions to write in `main.py`:**
  - `make_table(m)` → create a table with `m` empty buckets (lists).
  - `hash_basic(s)` → return a simple integer hash for a string.
  - `put(t, key, value)` → insert or overwrite `(key, value)`.
  - `get(t, key)` → return value or `None`.
  - `has_key(t, key)` → return `True/False`.
  - `size(t)` → total number of pairs in all buckets.
- **Inputs/Outputs:** Keys are **non-empty strings** (barcodes). Values are strings (titles).
- **Constraints:**  
  - Use only Python standard library.  
  - Do not mutate input keys/values.  
  - `m` (bucket count) is an integer `2 ≤ m ≤ 97`.
- **Expected complexity:** Average **O(1)** for `put/get/has_key`; worst-case **O(n)** when many collisions.

---

## ESL scaffold — The 8 Steps
**Steps 1–5: explicit**
1. **Read & Understand:** We need fast barcode → title lookup.  
2. **Re-phrase:** Jump to a **bucket** using a number from the barcode.  
3. **Identify I/O/vars:** Input: `key`, `value`, `table`; Output: value or `None`. Variables: `index`, `bucket`.  
4. **Break down:** Build `m` buckets. Compute `index = hash_basic(key) % m`. In the bucket, update if key exists; else append `[key, value]`.  
5. **Pseudocode:**  
```
t = [ [] for _ in range(m) ]

i = hash_basic(key) % m

for pair in t[i]:

if pair[0] == key: pair[1] = value; return

t[i].append([key, value])
```

**Steps 6–8: hints**

6. **Write code:** Follow pseudocode; keep it small.  

7. **Debug:** Try two keys that collide; check bucket contents.  
8. **Optimize:** Choose a larger `m` to reduce collisions.

---

## Hints
- Use `ord(ch)` to turn each character into a number for `hash_basic`.
- Overwrite when the key already exists in its bucket.
- Return `None` in `get` when key is not found (do not raise).

---

## How to run tests locally
```
python -m pytest -q

```

---

## FAQ
**Q1. Environment?** Python 3.10 or 3.11. No external libraries.  
**Q2. Read from stdin?** No. Implement functions and return values. Tests import your functions.  
**Q3. Big-O expectations?** Average `put/get/has_key` should be **O(1)**, worst-case **O(n)**.  
**Q4. Common pitfalls?** Forgetting to **overwrite** when keys match; forgetting to **return `None`** when missing; not scanning the bucket.  
**Q5. Grading?** Autograder runs pytest. All tests must pass.  
**Q6. Pytest failures?** Read the **assert message**: it shows expected vs actual. Re-run locally.  
**Q7. May I change function names?** No. Use the exact names shown above.