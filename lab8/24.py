import sqlite3

conn = sqlite3.connect("students.db")
average = conn.execute("SELECT AVG(marks) FROM students").fetchone()[0]
print("Average marks:", average)
conn.close()