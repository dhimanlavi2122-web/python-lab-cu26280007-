import sqlite3

conn = sqlite3.connect("students.db")
for student in conn.execute(
    "SELECT * FROM students ORDER BY marks DESC LIMIT 3"
):
    print(student)
conn.close()