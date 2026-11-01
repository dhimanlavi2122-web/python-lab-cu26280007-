import sqlite3

conn = sqlite3.connect("students.db")
rows = conn.execute("""
SELECT age, COUNT(*)
FROM students
GROUP BY age
""")

for row in rows:
    print("Age:", row[0], "Student count:", row[1])

conn.close()