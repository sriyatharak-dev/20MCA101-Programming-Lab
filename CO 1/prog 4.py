line = input("Enter a line: ").lower().split()
freq = {}
for word in line:
    freq[word] = freq.get(word, 0) + 1
print(freq)
