def program_10():
    with open("sample.txt", "r", encoding="utf-8") as file:
        print(file.read().upper())
