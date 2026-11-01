import sqlite3

roll = int(input("Enter roll number to delete: "))

connection = sqlite3.connect("school.db")
cursor = connection.cursor()

cursor.execute("DELETE FROM students WHERE roll = ?", (roll,))

connection.commit()
print("Student deleted." if cursor.rowcount else "Student not found.")

connection.close()