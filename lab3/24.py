numbers = list(map(int, input("Enter numbers: ").split()))

reverse = []

for i in range(len(numbers) - 1, -1, -1):
    reverse.append(numbers[i])

print("Reversed list:", reverse)