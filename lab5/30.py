t1 = (10, 20, 30)
t2 = (1, 2, 3)

result = ()

for i in range(len(t1)):
    result = result + (t1[i] + t2[i],)

print(result)
