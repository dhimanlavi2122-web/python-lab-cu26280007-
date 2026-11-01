def program_12():
    import re

    word = input("Enter the word to count: ")
    with open("sample.txt", "r", encoding="utf-8") as file:
        content = file.read()

    count = len(re.findall(
        r"\b" + re.escape(word) + r"\b",
        content,
        re.IGNORECASE
    ))
    print("Occurrences:", count)

