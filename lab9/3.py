students = [
    {"roll": "101", "name": "Asha", "marks": 85},
    {"roll": "102", "name": "Ravi", "marks": 92}
]

search_name = input("Enter student name: ").strip().lower()

found = False
for student in students:
    if student["name"].lower() == search_name:
        print(student)
        found = True

if not found:
    print("Student not found.")