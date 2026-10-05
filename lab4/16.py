data = {"A": 30, "B": 10, "C": 20}

result = dict(sorted(data.items(), key=lambda x: x[1]))

print(result)