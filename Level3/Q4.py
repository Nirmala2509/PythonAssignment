'''Define a class named Shape and its subclass Square. The Square
class has an init function which takes length as argument. Both
classes have an area function which can print the area of the
shape where Shape’s area is 0 by default.'''

class Shape:
    def area(self):
        return 0  # Default area for a generic shape

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

# Test the classes
s1 = Shape()
print("Area of Shape:", s1.area())  # Output: 0

s2 = Square(5)
print("Area of Square:", s2.area())  # Output: 25
