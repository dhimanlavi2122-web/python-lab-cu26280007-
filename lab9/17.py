import sqlite3

connection = sqlite3.connect("school.db")
cursor = connection.cursor()

cursor.execute("SELECT COUNT(*) FROM students")
total = cursor.fetchone()[0]

print("Total student records:", total)

connection.close()