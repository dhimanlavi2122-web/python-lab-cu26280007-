t1 = (10, 20, 30, 40)
t2 = (30, 40, 50, 60)

difference = ()

for x in t1:
    if x not in t2:
        difference = difference + (x,)

print(difference)
