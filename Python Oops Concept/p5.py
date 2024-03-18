
#wap to create a class name 'rectangle'. in rectangle take two instance variables
# length and breadth. Now create a method area() and perimeter() the area and perimeter.

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

# Creating an instance of Rectangle
my_rectangle = Rectangle(5, 10)

# Calculating area and perimeter
print("Area of the rectangle:", my_rectangle.area())
print("Perimeter of the rectangle:", my_rectangle.perimeter())
