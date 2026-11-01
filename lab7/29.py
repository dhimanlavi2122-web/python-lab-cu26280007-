import csv
import glob
def program_29():
    name = input("Enter the student's name to search for: ").casefold()

    with open("students.csv", "r", newline="", encoding="utf-8") as file:
        matches = [
            row for row in csv.DictReader(file)
            if row.get("Name", "").casefold() == name
        ]

    if matches:
        for record in matches:
            print(record)
    else:
        print("Student not found.")
