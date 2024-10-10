# Using a function, create a program that calculates the volume of a cylinder.
import math

pie = math.pi 
radius = float(input("Enter the radius value: "))
height = float(input("Enter the height value: "))
cylinder_volume = pie * radius ** 2 * height
print(f"The volume of the cylinder with height {height} and radius {radius} is {cylinder_volume}")
    
    