def program_13():
    with open("numbers.txt", "r", encoding="utf-8") as file:
        numbers = [float(value) for value in file.read().split()]

    if numbers:
        print("Sum:", sum(numbers))
        print("Average:", sum(numbers) / len(numbers))
    else:
        print("The file contains no numbers.")
