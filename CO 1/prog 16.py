a = input("First string: ")
b = input("Second string: ")
if len(a) > 1 and len(b) > 1:
    a, b = a[0] + b[1] + a[2:], b[0] + a[1] + b[2:]
print(a + " " + b)
