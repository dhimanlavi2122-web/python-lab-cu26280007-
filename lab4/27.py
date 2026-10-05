data = {"A": 10, "B": 20, "C": 10, "D": 30}

new_data = {}

for key, value in data.items():
    if value not in new_data.values():
        new_data[key] = value

print(new_data)