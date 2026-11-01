import csv
import glob
def program_24():
    with open("students.csv", "r", newline="", encoding="utf-8") as file:
        rows = list(csv.reader(file))

    print("Data rows:", max(0, len(rows) - 1))
    print("Column count:", len(rows[0]) if rows else 0)

