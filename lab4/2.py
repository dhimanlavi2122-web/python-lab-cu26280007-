numbers = [1, 2, 3, 4, 5]
n = 2
print("Original list =", numbers)
rotated = numbers[n:] + numbers[:n]

print("Rotated list =", rotated)