nums = list(map(int, input("Enter integers: ").split()))
odd = [n for n in nums if n % 2 != 0]
print(odd)
