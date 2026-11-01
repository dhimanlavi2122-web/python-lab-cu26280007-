import sqlite3

roll = int(input("Enter roll number to search: "))

connection = sqlite3.connect("school.db")
cursor = connection.cursor()

cursor.execute("SELECT roll, name, marks FROM students WHERE roll = ?", (roll,))
student = cursor.fetchone()

if student:
    print(student)
else:
    print("Student not found.")

connection.close()