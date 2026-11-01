import csv
import glob
def program_28():
    with open("students.csv", "r", newline="", encoding="utf-8") as file:
        students = list(csv.DictReader(file))

    try:
        highest = max(students, key=lambda student: float(student["Marks"]))
        print("Highest marks:", highest["Name"], highest["Marks"])
    except (ValueError, KeyError):
        print("No valid Name and Marks records were found.")
