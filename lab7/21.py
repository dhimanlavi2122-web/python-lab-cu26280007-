import csv
import glob
def program_21():
    records = [
        ["Name", "Age", "Marks"],
        ["Asha", 18, 92],
        ["Ravi", 19, 85],
    ]

    with open("students.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(records)

    print("Data saved in students.csv.")

