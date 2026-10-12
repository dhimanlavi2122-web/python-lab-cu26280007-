my_set = {1, 2, 3}
power_set = [set()]

for item in my_set:
    new_subsets = []
    for subset in power_set:
        new_subsets.append(subset | {item})
    power_set.extend(new_subsets)

print("Power set:", power_set)