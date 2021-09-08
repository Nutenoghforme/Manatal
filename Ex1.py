#Exercise 1: Object Oriented Programming
#Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle.
import math
class Circle():
    def __init__(it,radius):
        it.radius=radius
    def area(it):
        return math.pi*(it.radius**2)
    def perimeter(it):
        return 2*math.pi*it.radius
        
r = int(input("Enter radius of circle = "))
obj = Circle(r)
        
print("Area of circle = ",round(obj.area(),2))
print("Perimeter of circle = ",round(obj.perimeter(),2)) 