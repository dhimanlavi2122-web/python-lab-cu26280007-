import sqlite3

connection = sqlite3.connect("school.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        roll INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        marks REAL NOT NULL
    )
""")

connection.commit()
connection.close()

print("Connected to database and created students table.")