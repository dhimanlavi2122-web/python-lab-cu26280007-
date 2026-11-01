def program_3():
    with open("sample.txt", "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")

