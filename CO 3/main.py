import graphics.rectangle as rect

from graphics.circle import area as circle_area
from graphics.circle import perimeter as circle_perimeter

from graphics.three_d_graphics.cuboid import *

import graphics.three_d_graphics.sphere as sph

# Rectangle
print("RECTANGLE")
l = float(input("Enter length: "))
b = float(input("Enter breadth: "))

print("Area:", rect.area(l, b))
print("Perimeter:", rect.perimeter(l, b))

# Circle
print("\nCIRCLE")
r = float(input("Enter radius: "))

print("Area:", circle_area(r))
print("Perimeter:", circle_perimeter(r))

# Cuboid
print("\nCUBOID")
l = float(input("Enter length: "))
b = float(input("Enter breadth: "))
h = float(input("Enter height: "))

print("Surface Area:", area(l, b, h))
print("Total Edge Length:", perimeter(l, b, h))

# Sphere
print("\nSPHERE")
r = float(input("Enter radius: "))

print("Surface Area:", sph.area(r))
print("Circumference:", sph.perimeter(r))