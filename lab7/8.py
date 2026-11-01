def program_8():
    with open("sample.txt", "a", encoding="utf-8") as file:
        file.write(input("Enter content to append: ") + "\n")
    print("Content appended.")


