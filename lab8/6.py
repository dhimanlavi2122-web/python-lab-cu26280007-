import sqlite3

conn = sqlite3.connect("students.db")
conn.execute("DROP TABLE IF EXISTS students")
conn.commit()
print("students table deleted.")
conn.close()