import csv
import glob
def program_25():
    name = input("Enter the student's name: ")
    age = input("Enter the student's age: ")
    marks = input("Enter the student's marks: ")

    with open("students.csv", "a", newline="", encoding="utf-8") as file:
        csv.writer(file).writerow([name, age, marks])

    print("Record added to students.csv.")

