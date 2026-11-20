words = input("Enter words: ").split()
if words:
    print("Length =", len(max(words, key=len)))
else:
    print("No words entered")
