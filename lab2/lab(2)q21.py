n=int(input("enter a number:"))
total=0
n = abs(n)
while n> 0:
    total += n % 10
    n //= 10
print("Sum of digits =", total)


