import math

class Shape:
    
    
    def __init__(self, name):
        self.name = name
    
    def area(self):
      
        raise NotImplementedError("Subclasses must implement the area() method")
    
    def __str__(self):
        return f"{self.name} with area: {self.area()}"


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width
    
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    
 
    def area(self):
        
        return math.pi * self.radius ** 2
        
    
    def circumference(self):
        
        return 2 * math.pi * self.radius