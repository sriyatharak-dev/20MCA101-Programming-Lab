import math
start = int(input("Start: "))
end = int(input("End: "))
for n in range(max(1000, start), min(9999, end) + 1):
    r = math.isqrt(n)
    if r * r == n and all(int(d) % 2 == 0 for d in str(n)):
        print(n, end=" ")
