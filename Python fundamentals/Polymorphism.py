from abc import ABC, abstractmethod
import math

class Shape():
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        print(f"The area of the circle is: {self.radius*math.pi} cm² ")

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        print(f"The area of the rectangle is {self.width*self.height} cm²")

class Pizza(Circle):
    def __init__(self,toppings,radius):
        super().__init__(radius)
        self.toppings = toppings
    def area(self):
        print(f"The topping on this is {self.toppings} ")
        super().area()


pepporoni_pizza = Pizza('pepporoni',10)
pepporoni_pizza.area()