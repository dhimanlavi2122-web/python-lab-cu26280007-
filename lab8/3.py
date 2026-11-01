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
conn.commit()
print("students table created!")
conn.close()