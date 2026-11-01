import sqlite3

student_id = int(input("Student ID: "))
new_marks = float(input("New marks: "))

conn = sqlite3.connect("students.db")
conn.execute(
    "UPDATE students SET marks=? WHERE id=?",
    (new_marks, student_id)
)
conn.commit()
print("Marks updated.")
conn.close()