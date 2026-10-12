t = ((1, 2), (3, 4), (5, 6))

result = ()

for x in t:
    for y in x:
        result = result + (y,)

print(result)
