num = int(input("Enter a number: "))
if num == 0:
    count = 1
else:
    count = 0
    num = abs(num)
    while num > 0:
        count += 1
        num //= 10
print("Number of digits =", count)

