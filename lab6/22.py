list22 = [1, 2, 2, 3, 4, 4, 4]
seen = set()
duplicates = set()

for item in list22:
    if item in seen:
        duplicates.add(item)
    else:
        seen.add(item)

print("22.", duplicates)

