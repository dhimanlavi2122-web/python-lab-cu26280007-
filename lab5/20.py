t = ("apple", "banana", "cat", "elephant")

longest = 0

for word in t:
    if len(word) > longest:
        longest = len(word)

print("Length =", longest)
