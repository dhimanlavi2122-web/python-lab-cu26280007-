def program_15():
    old_word = input("Enter the word to replace: ")
    new_word = input("Enter the replacement word: ")

    with open("sample.txt", "r", encoding="utf-8") as file:
        content = file.read()

    with open("sample.txt", "w", encoding="utf-8") as file:
        file.write(content.replace(old_word, new_word))

    print("Word replaced.")

