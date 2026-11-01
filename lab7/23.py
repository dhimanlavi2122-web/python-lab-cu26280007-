import csv
import glob
def program_23():
    with open("students.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        columns = reader.fieldnames or []

    for column in columns:
        try:
            values = [float(row[column]) for row in rows]
        except (ValueError, TypeError):
            continue

        if values:
            print(f"{column} average:", sum(values) / len(values))
