import csv
import glob
def program_22():
    with open("students.csv", "r", newline="", encoding="utf-8") as file:
        for row in csv.reader(file):
            print(", ".join(row))

