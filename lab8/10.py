import sqlite3

conn = sqlite3.connect("students.db")
for student in conn.execute("SELECT * FROM students"):
    print(student)
conn.close()