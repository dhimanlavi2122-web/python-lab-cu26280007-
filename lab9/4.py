students = [
    {"roll": "101", "name": "Asha", "marks": 85},
    {"roll": "102", "name": "Ravi", "marks": 92}
]

roll = input("Enter roll number: ")
found = False

for student in students:
    if student["roll"] == roll:
        student["marks"] = float(input("Enter new marks: "))
        print("Marks updated.")
        print(student)
        found = True
        break

if not found:
    print("Student not found.")