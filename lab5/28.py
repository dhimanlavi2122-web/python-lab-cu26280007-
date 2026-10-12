t = (10, 20, 10, 30, 20, 40)

repeated = ()

for x in t:
    if t.count(x) > 1 and x not in repeated:
        repeated = repeated + (x,)

print(repeated)
