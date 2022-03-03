# importing all modules
from CirFunctions import *

# importing selective
from CuboidFunctions import CuboidArea,CuboidPerimeter

# normal importing
import RectFunctions as rect
import SphereFunctions as sph

print(" ")
l = int(input("Enter the length of Rectangle: "))
b = int(input("Enter the breadth of Rectangle: "))
print("Area = ", rect.RectArea(l, b))
print("Perimeter =", rect.RectPerimeter(l, b))

print(" ")

#
r = int(input("Enter the radius of a circle: "))
print("Circle area = ", CirArea(r))
print("Circle Perimeter = ", CirPerimeter(r))

print(" ")

r = int(input("Enter the radius of Sphere: "))
print("Sphere area = ", sph.SpArea(r))
print("Sphere Perimeter = ", sph.SpPerimeter(r))

print(" ")

l = int(input("Enter the  length of Cuboid: "))
b = int(input("Enter the breadth of Cuboid: "))
h = int(input("Enter the height of Cuboid: "))
print("Cuboid area = ", CuboidArea(l, b, h))
print("Cuboid Perimeter = ", CuboidPerimeter(l, b, h))
