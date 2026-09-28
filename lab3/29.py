list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

difference = []

for num in list1:
    if num not in list2:
        difference.append(num)

print("Difference:", difference)