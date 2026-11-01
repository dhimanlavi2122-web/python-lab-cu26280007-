import sqlite3

connection = sqlite3.connect("school.db")
cursor = connection.cursor()

cursor.execute("SELECT roll, name, marks FROM students ORDER BY name")
for student in cursor.fetchall():
    print(student)

connection.close()