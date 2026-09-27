a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    lcm = a
else:
    lcm = b
while True:
    if lcm % a == 0 and lcm % b == 0:
        break
    lcm += 1
print("LCM =", lcm)
