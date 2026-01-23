class Shape:
    
    
    def __init__(self, name):
        self.name = name
    
    def area(self):
        """
        Calculate the area of the shape.
        This method MUST be overridden in child classes.
        """
        raise NotImplementedError("Subclasses must implement the area() method")
    
    def __str__(self):
        return f"{self.name} with area: {self.area()}"


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width
    
    # Override the area() method
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    
    # Override the area() method
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def circumference(self):
        return 2 * 3.14159 * self.radius