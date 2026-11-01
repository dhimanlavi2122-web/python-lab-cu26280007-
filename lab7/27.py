import csv
import glob
def program_27():
    with open("students.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        if not {"Name", "Marks"}.issubset(reader.fieldnames or []):
            print("The CSV file must contain Name and Marks columns.")
            return

        for row in reader:
            print(row["Name"], row["Marks"], sep=": ")

