import sqlite3

roll = int(input("Enter roll number: "))
marks = float(input("Enter new marks: "))

connection = sqlite3.connect("school.db")
cursor = connection.cursor()

cursor.execute(
    "UPDATE students SET marks = ? WHERE roll = ?",
    (marks, roll)
)

connection.commit()
print("Marks updated." if cursor.rowcount else "Student not found.")

connection.close()