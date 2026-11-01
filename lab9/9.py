with open("students.txt", "w", encoding="utf-8") as file:
    count = int(input("How many students? "))

    for _ in range(count):
        roll = input("Roll number: ")
        name = input("Name: ")
        marks = input("Marks: ")
        file.write(f"{roll},{name},{marks}\n")

print("\nStudent records from file:")

with open("students.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())