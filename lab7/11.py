def program_11():
    word = input("Enter the word to search for: ")
    with open("sample.txt", "r", encoding="utf-8") as file:
        content = file.read()

    if word.casefold() in content.casefold():
        print("Word found.")
    else:
        print("Word not found.")
