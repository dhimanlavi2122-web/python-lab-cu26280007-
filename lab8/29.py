import sqlite3


def insert_student(conn, name, age, marks):
    conn.execute(
        "INSERT INTO students (name, age, marks) VALUES (?, ?, ?)",
        (name, age, marks)
    )
    conn.commit()


def fetch_students(conn):
    return conn.execute("SELECT * FROM students").fetchall()


conn = sqlite3.connect("students.db")

insert_student(conn, "Neha", 18, 88)

for student in fetch_students(conn):
    print(student)

conn.close()