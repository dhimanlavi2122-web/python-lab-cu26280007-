import sqlite3

conn = sqlite3.connect("students.db")
conn.execute("""
CREATE TABLE IF NOT EXISTS courses (
    id INTEGER PRIMARY KEY,
    student_id INTEGER,
    course_name TEXT
)
""")

conn.execute(
    "INSERT INTO courses (student_id, course_name) VALUES (?, ?)",
    (1, "Python")
)
conn.commit()
print("Courses table created and course added.")
conn.close()