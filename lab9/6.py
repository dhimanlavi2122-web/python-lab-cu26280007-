employees = {}

while True:
    print("\n1. Add  2. View  3. Update  4. Delete  0. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        employee_id = input("Employee ID: ")
        name = input("Name: ")
        salary = float(input("Salary: "))
        employees[employee_id] = {"name": name, "salary": salary}
        print("Employee added.")

    elif choice == "2":
        for employee_id, details in employees.items():
            print(employee_id, details)

    elif choice == "3":
        employee_id = input("Employee ID to update: ")
        if employee_id in employees:
            employees[employee_id]["name"] = input("New name: ")
            employees[employee_id]["salary"] = float(input("New salary: "))
            print("Employee updated.")
        else:
            print("Employee not found.")

    elif choice == "4":
        employee_id = input("Employee ID to delete: ")
        if employee_id in employees:
            del employees[employee_id]
            print("Employee deleted.")
        else:
            print("Employee not found.")

    elif choice == "0":
        break

    else:
        print("Invalid choice.")