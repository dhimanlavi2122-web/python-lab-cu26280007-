text = "hello"

data = {}

for ch in text:
    if ch in data:
        data[ch] = data[ch] + 1
    else:
        data[ch] = 1

print(data)