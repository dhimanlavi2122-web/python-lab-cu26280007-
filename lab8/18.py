import sqlite3

student_id = int(input("Student ID to delete: "))

conn = sqlite3.connect("students.db")
conn.execute("DELETE FROM students WHERE id=?", (student_id,))
conn.commit()
print("Student deleted.")
conn.close()