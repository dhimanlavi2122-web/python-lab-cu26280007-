s = input("Enter a string: ")
result = ""
new_word = True

for ch in s:
    if ch == " ":
        result += ch
        new_word = True
    elif new_word:
        result += ch.upper()
        new_word = False
    else:
        result += ch.lower()

print(result)