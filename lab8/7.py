import sqlite3

conn = sqlite3.connect("students.db")
result = conn.execute(
    "SELECT name FROM sqlite_master WHERE type='table' AND name=?",
    ("students",)
).fetchone()

if result:
    print("students table exists.")
else:
    print("students table does not exist.")

conn.close()