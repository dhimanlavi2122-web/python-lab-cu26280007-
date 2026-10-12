from collections import Counter

word1 = "listen"
word2 = "silent"

if Counter(word1.lower()) == Counter(word2.lower()):
    print("The strings are anagrams")
else:
    print("The strings are not anagrams")