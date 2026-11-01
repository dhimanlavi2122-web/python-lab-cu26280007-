import csv
import sqlite3

conn = sqlite3.connect("students.db")
rows = conn.execute("SELECT * FROM students").fetchall()

with open("students.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["id", "name", "age", "marks"])
    writer.writerows(rows)

print("Data exported to students.csv.")
conn.close()