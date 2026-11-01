def program_16():
    with open("sample.txt", "r", encoding="utf-8") as file:
        lines = file.read().splitlines()

    if lines:
        print("First line:", lines[0])
        print("Last line:", lines[-1])
    else:
        print("The file is empty.")


