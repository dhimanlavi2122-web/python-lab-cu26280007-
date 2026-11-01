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

students = [
    ("Ravi", 20, 78),
    ("Mina", 19, 86),
    ("Asha", 18, 93)
]

conn.executemany(
    "INSERT INTO students (name, age, marks) VALUES (?, ?, ?)",
    students
)
conn.commit()
print("Multiple students added.")
conn.close()