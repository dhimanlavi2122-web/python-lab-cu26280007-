data = {"A": 10, "B": 20, "C": 30}

new_data = {}

for key, value in data.items():
    new_data[value] = key

print(new_data)