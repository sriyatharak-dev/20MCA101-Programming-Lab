name = input("Enter file name: ")
if "." in name:
    print("Extension:", name.rsplit(".", 1)[1])
else:
    print("No extension")
