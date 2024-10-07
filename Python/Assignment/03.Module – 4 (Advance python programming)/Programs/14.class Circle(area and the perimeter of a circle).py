# Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle

class Circle:
    def area(self, radius):
            # Calculate and print the area of the circle
        print(f"Area of Circle: {3.14 * radius * radius}")
        
    def perimeter(self, radius):
            # Calculate and print the perimeter of the circle
        print(f"Perimeter of Circle: {2 * 3.14 * radius}")

    # get the radius from the users.
r = int(input("Enter Radius of Circle: "))

    # Create an instance of Circle
obj = Circle()

    # Call the area method.
obj.area(r)

    # Call the perimeter method to print the perimeter.
obj.perimeter(r)
