import sqlite3

conn = sqlite3.connect("students.db")
for column in conn.execute("PRAGMA table_info(students)"):
    print(column)
conn.close()