# Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle.

class Rectangle:
    def __init__(self, length, width):
            # Initialize the length and width attributes
        self.length = length 
        self.width = width

    def area(self):
            # Calculate and print the area of the rectangle
        print(f"Area of a Rectangle : {self.width * self.length}")


    # get length and width from the user.
l = int(input("Enter a Length : "))
w = int(input("Enter a Width  : "))

    # Create an object of class.
obj = Rectangle(l, w)

    # Call the area method.
obj.area()
