import sqlite3

conn = sqlite3.connect("students.db")
rows = conn.execute("""
SELECT students.name, courses.course_name
FROM students
LEFT JOIN courses ON students.id = courses.student_id
""")

for row in rows:
    print(row)

conn.close()