numbers = list(map(int, input("Enter numbers: ").split()))

unique = list(set(numbers))
unique.sort()

print("Second largest:", unique[-2])