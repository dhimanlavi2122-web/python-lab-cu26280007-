import json
import os

FILE_NAME = "records.json"

def read_records():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        return json.load(file)

def save_records(records):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(records, file, indent=4)

while True:
    print("\n1. Add  2. View  3. Modify  4. Delete  0. Exit")
    choice = input("Choose an option: ")
    records = read_records()

    if choice == "1":
        record_id = input("Record ID: ")
        name = input("Name: ")
        records.append({"id": record_id, "name": name})
        save_records(records)
        print("Record added.")

    elif choice == "2":
        for record in records:
            print(record)

    elif choice == "3":
        record_id = input("Record ID to modify: ")
        record = next((r for r in records if r["id"] == record_id), None)
        if record:
            record["name"] = input("New name: ")
            save_records(records)
            print("Record modified.")
        else:
            print("Record not found.")

    elif choice == "4":
        record_id = input("Record ID to delete: ")
        updated_records = [r for r in records if r["id"] != record_id]
        if len(updated_records) < len(records):
            save_records(updated_records)
            print("Record deleted.")
        else:
            print("Record not found.")

    elif choice == "0":
        break

    else:
        print("Invalid choice.")