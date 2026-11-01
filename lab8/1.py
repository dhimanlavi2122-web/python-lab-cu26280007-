import sqlite3

conn = sqlite3.connect("students.db")
print("Database connected successfully!")
conn.close()