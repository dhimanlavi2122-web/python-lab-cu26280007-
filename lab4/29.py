dict1 = {"A": 10, "B": 20, "C": 30}
dict2 = {"B": 40, "C": 50, "D": 60}

for key in dict1:
    if key in dict2:
        print(key)