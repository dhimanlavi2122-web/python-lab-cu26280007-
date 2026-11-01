import sqlite3

connection = sqlite3.connect("school.db")
cursor = connection.cursor()

cursor.execute("""
    SELECT roll, name, marks
    FROM students
    WHERE marks = (SELECT MAX(marks) FROM students)
""")

students = cursor.fetchall()

if students:
    for student in students:
        print(student)
else:
    print("No student records found.")

connection.close()