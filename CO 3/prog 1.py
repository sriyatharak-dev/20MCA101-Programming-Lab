import math
import random
import datetime

n = int(input("Enter a number: "))

print("Square root:", math.sqrt(n))
print("Factorial:", math.factorial(n))

a = int(input("Enter starting range: "))
b = int(input("Enter ending range: "))

print("Random number:", random.randint(a, b))

today = datetime.datetime.now()
print("Current date and time:", today)