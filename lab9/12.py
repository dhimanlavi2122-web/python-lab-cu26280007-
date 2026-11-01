import sqlite3

roll = int(input("Roll number: "))
name = input("Name: ")
marks = float(input("Marks: "))

connection = sqlite3.connect("school.db")
cursor = connection.cursor()

cursor.execute(
    "INSERT INTO students (roll, name, marks) VALUES (?, ?, ?)",
    (roll, name, marks)
)

connection.commit()
connection.close()

print("Student record added.")