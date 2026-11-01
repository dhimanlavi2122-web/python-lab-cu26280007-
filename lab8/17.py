import sqlite3

student_id = int(input("Student ID: "))
new_name = input("New name: ")

conn = sqlite3.connect("students.db")
conn.execute(
    "UPDATE students SET name=? WHERE id=?",
    (new_name, student_id)
)
conn.commit()
print("Name updated.")
conn.close()