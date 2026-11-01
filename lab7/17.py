def program_17():
    with open("sample.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    with open("sample.txt", "w", encoding="utf-8") as file:
        file.writelines(line for line in lines if line.strip())

    print("Blank lines removed.")
