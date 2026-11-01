import sqlite3

conn = sqlite3.connect("students.db")
conn.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    marks REAL
)
""")

conn.execute(
    "INSERT INTO students (name, age, marks) VALUES (?, ?, ?)",
    ("Asha", 19, 92)
)
conn.commit()
print("One student added.")
conn.close()