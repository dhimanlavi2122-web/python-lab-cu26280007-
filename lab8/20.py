import sqlite3

conn = sqlite3.connect("students.db")
conn.execute("DELETE FROM students")
conn.commit()
print("All student records deleted; table structure remains.")
conn.close()