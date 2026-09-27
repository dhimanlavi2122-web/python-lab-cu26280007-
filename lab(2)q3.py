num = int(input("Enter a number: "))
original = num
digits = 0
temp = num
while temp > 0:
    digits += 1
    temp //= 10
temp = num
total = 0
while temp > 0:
    digit = temp % 10
    total += digit ** digits
    temp //= 10
if total == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
