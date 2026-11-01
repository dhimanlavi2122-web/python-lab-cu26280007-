def program_18():
    with open("sample.txt", "r", encoding="utf-8") as file:
        words = file.read().split()

    unique_words = list(dict.fromkeys(words))

    with open("unique_words.txt", "w", encoding="utf-8") as file:
        file.write("\n".join(unique_words))
        if unique_words:
            file.write("\n")

    print("Unique words saved in unique_words.txt.")
