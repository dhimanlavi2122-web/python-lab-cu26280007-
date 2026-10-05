numbers = [[1, 2], [3, 4], [5, 6]]

flat = []

for x in numbers:
    for y in x:
        flat.append(y)

print("Flattened list =", flat)