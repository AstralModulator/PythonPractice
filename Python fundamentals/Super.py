#Super Function
class Shapes:
    def __init__(self, is_filled,color):
        self.is_filled = is_filled
        self.color = color
    def describe(self):
        print(f"The shape is {'filled' if self.is_filled else 'unfilled'} with color {self.color}")
class Circle(Shapes):
    def __init__(self,is_filled,color,radius):
        super().__init__(is_filled,color)
        self.radius = radius
    def describe(self):
        print(f"This is circle with radius {self.radius}")
        super().describe()

circle = Circle(True,"red",10)
circle.describe()
