import sqlite3

conn = sqlite3.connect("students.db")
conn.execute("DELETE FROM students WHERE marks < 40")
conn.commit()
print("Students with marks below 40 deleted.")
conn.close()