import sqlite3

conn = sqlite3.connect("students.db")
conn.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    marks REAL
)
""")
conn.commit()

while True:
    print("\n1. Add student")
    print("2. View students")
    print("3. Delete student")
    print("4. Update student marks")
    print("0. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Name: ")
        age = int(input("Age: "))
        marks = float(input("Marks: "))
        conn.execute(
            "INSERT INTO students (name, age, marks) VALUES (?, ?, ?)",
            (name, age, marks)
        )
        conn.commit()
        print("Student added.")

    elif choice == "2":
        for student in conn.execute("SELECT * FROM students"):
            print(student)

    elif choice == "3":
        student_id = int(input("Student ID to delete: "))
        conn.execute("DELETE FROM students WHERE id=?", (student_id,))
        conn.commit()
        print("Student deleted.")

    elif choice == "4":
        student_id = int(input("Student ID: "))
        marks = float(input("New marks: "))
        conn.execute(
            "UPDATE students SET marks=? WHERE id=?",
            (marks, student_id)
        )
        conn.commit()
        print("Marks updated.")

    elif choice == "0":
        break

    else:
        print("Invalid choice.")

conn.close()