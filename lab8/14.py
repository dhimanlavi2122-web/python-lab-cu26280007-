import sqlite3

conn = sqlite3.connect("students.db")
count = conn.execute("SELECT COUNT(*) FROM students").fetchone()[0]
print("Total students:", count)
conn.close()