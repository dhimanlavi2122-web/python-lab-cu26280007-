def program_14():
    with open("sample.txt", "r", encoding="utf-8") as file:
        lines = file.read().splitlines()

    if lines:
        longest = max(lines, key=len)
        print("Longest line:", longest)
        print("Character count:", len(longest))
    else:
        print("The file is empty.")

