def program_20():
    first_file = input("Enter the first file name: ")
    second_file = input("Enter the second file name: ")

    with open("merged.txt", "w", encoding="utf-8") as output:
        for filename in (first_file, second_file):
            with open(filename, "r", encoding="utf-8") as source:
                output.write(source.read())
                output.write("\n")

    print("Files merged into merged.txt.")
