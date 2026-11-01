def program_7():
    print("Enter lines. Type .done on a separate line when finished:")
    lines = []
    while True:
        line = input()
        if line == ".done":
            break
        lines.append(line)

    with open("sample.txt", "w", encoding="utf-8") as file:
        file.write("\n".join(lines))
        if lines:
            file.write("\n")
    print("Lines saved in sample.txt.")


