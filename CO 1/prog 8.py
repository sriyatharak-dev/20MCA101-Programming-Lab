s = input("Enter a string: ")
if s:
    first = s[0]
    result = first + s[1:].replace(first, "$")
    print(result)
else:
    print("")
