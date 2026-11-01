def program_4():
    with open("sample.txt", "r", encoding="utf-8") as file:
        print("Word count:", len(file.read().split()))

