colors = input("Enter colors separated by commas: ").split(",")
colors = [c.strip() for c in colors]
if colors:
    print("First:", colors[0])
    print("Last:", colors[-1])
