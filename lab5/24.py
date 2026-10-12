t1 = (10, 20, 30, 40)
t2 = (30, 40, 50, 60)

common = ()

for x in t1:
    if x in t2:
        common = common + (x,)

print(common)
