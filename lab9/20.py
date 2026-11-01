import sqlite3

connection = sqlite3.connect("school.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        roll INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        marks REAL NOT NULL
    )
""")
connection.commit()

while True:
    print("\n1. Add student")
    print("2. View all students")
    print("3. Search by roll number")
    print("4. Update marks")
    print("5. Delete student")
    print("0. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        roll = int(input("Roll number: "))
        name = input("Name: ")
        marks = float(input("Marks: "))

        try:
            cursor.execute(
                "INSERT INTO students (roll, name, marks) VALUES (?, ?, ?)",
                (roll, name, marks)
            )
            connection.commit()
            print("Student added.")
        except sqlite3.IntegrityError:
            print("That roll number already exists.")

    elif choice == "2":
        cursor.execute("SELECT roll, name, marks FROM students")
        for student in cursor.fetchall():
            print(student)

    elif choice == "3":
        roll = int(input("Roll number: "))
        cursor.execute(
            "SELECT roll, name, marks FROM students WHERE roll = ?",
            (roll,)
        )
        student = cursor.fetchone()
        print(student if student else "Student not found.")

    elif choice == "4":
        roll = int(input("Roll number: "))
        marks = float(input("New marks: "))
        cursor.execute(
            "UPDATE students SET marks = ? WHERE roll = ?",
            (marks, roll)
        )
        connection.commit()
        print("Marks updated." if cursor.rowcount else "Student not found.")

    elif choice == "5":
        roll = int(input("Roll number to delete: "))
        cursor.execute("DELETE FROM students WHERE roll = ?", (roll,))
        connection.commit()
        print("Student deleted." if cursor.rowcount else "Student not found.")

    elif choice == "0":
        break

    else:
        print("Invalid choice.")

connection.close()