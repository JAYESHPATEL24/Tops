import turtle
import time

# Set up the screen
screen = turtle.Screen()
screen.title("Thank You Card")
screen.bgcolor("lightblue")

# Create a turtle object
pen = turtle.Turtle()
pen.speed(2)
pen.color("blue")

# Write the gratitude message letter by letter
message = "Thank You for being an Amazing Soft Skill Teacher!"
pen.penup()
pen.goto(0, 0)
pen.pendown()

for char in message:
    pen.write(char, move=True, align="center", font=("Arial", 20, "normal"))
    time.sleep(0.2)

pen.hideturtle()
screen.mainloop()
