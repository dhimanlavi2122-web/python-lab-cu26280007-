students = []

n = int(input("How many students? "))

for _ in range(n):
    roll = input("Roll number: ")
    name = input("Name: ")
    marks = float(input("Marks: "))

    students.append({
        "roll": roll,
        "name": name,
        "marks": marks
    })

print("Student records created.")