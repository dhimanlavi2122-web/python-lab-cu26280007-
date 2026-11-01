def program_5():
    with open("sample.txt", "r", encoding="utf-8") as file:
        content = file.read()
    print("Line count:", len(content.splitlines()))
    print("Character count:", len(content))
