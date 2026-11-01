import sqlite3

connection = sqlite3.connect("school.db")
cursor = connection.cursor()

cursor.execute("SELECT roll, name, marks FROM students")
students = cursor.fetchall()

for student in students:
    print(student)

connection.close()