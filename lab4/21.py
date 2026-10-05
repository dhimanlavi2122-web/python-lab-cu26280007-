data = {"A": 50, "B": 80, "C": 60}

key = max(data, key=data.get)

print("Key =", key)