students = [
    {"roll": "101", "name": "Asha", "marks": 85},
    {"roll": "102", "name": "Ravi", "marks": 92}
]

roll = input("Enter roll number to delete: ")
old_count = len(students)

students = [student for student in students if student["roll"] != roll]

if len(students) < old_count:
    print("Student deleted.")
else:
    print("Student not found.")

print(students)