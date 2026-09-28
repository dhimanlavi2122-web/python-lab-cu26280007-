numbers = list(map(int, input("Enter numbers: ").split()))

print("Ascending:", sorted(numbers))
print("Descending:", sorted(numbers, reverse=True))