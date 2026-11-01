def program_19():
    with open("sample.txt", "r", encoding="utf-8") as file:
        words = file.read().split()

    words.sort(key=str.casefold)

    with open("sorted_words.txt", "w", encoding="utf-8") as file:
        file.write("\n".join(words))
        if words:
            file.write("\n")

    print("Sorted words saved in sorted_words.txt.")
