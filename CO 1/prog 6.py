names = input("Enter first names: ").split()
count = sum(name.lower().count("a") for name in names)
print("Count of a:", count)
