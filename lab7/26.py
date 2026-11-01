import csv
import glob
def program_26():
    source_name = input("Enter the source CSV file name: ")
    destination_name = input("Enter the destination CSV file name: ")

    with open(source_name, "r", newline="", encoding="utf-8") as source:
        rows = list(csv.reader(source))

    with open(destination_name, "w", newline="", encoding="utf-8") as destination:
        csv.writer(destination).writerows(rows)

    print("CSV data copied.")

