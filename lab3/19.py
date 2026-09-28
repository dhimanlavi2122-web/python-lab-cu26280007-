s = input("Enter a sentence: ")
words = s.lower().split()

freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

most_repeated = max(freq, key=freq.get)

print("Most repeated word:", most_repeated)