def program_1():
    with open("sample.txt", "w", encoding="utf-8") as file:
        file.write(input("Enter text: "))
    print("Text saved in sample.txt.")
