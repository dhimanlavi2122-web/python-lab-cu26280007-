import sqlite3

conn = sqlite3.connect("students.db")
print("Database created successfully!")
conn.close()