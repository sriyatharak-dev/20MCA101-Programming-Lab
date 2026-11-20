a = input("First colors: ").split()
b = input("Second colors: ").split()
print([c for c in a if c not in b])
