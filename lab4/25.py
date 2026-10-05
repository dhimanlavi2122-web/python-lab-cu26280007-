text = "apple mango apple banana mango apple"

words = text.split()

freq = {}

for word in words:
    if word in freq:
        freq[word] = freq[word] + 1
    else:
        freq[word] = 1

print(freq)