import csv
import sqlite3

conn = sqlite3.connect("students.db")

with open("students.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        conn.execute(
            "INSERT INTO students (id, name, age, marks) VALUES (?, ?, ?, ?)",
            (row["id"], row["name"], row["age"], row["marks"])
        )

conn.commit()
print("CSV data imported.")
conn.close()