import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Thank You Card")
screen.bgcolor("lightblue")

# Create a turtle object
pen = turtle.Turtle()
pen.speed(2)  # Slow down the speed
pen.color("blue")

# Write the gratitude message
pen.penup()
pen.goto(0, 150)
pen.pendown()
pen.write("Thank You!", align="center", font=("Arial", 40, "bold"))

pen.penup()
pen.goto(0, 50)
pen.pendown()
pen.write("For Being an Amazing Soft Skill Teacher", align="center", font=("Arial", 20, "normal"))

# Draw a heart
pen.color("red")
pen.penup()
pen.goto(0, -100)
pen.pendown()
pen.speed(1)  # Slow down further for the heart

pen.begin_fill()
pen.left(140)
pen.forward(180)
pen.circle(-90, 200)
pen.left(120)
pen.circle(-90, 200)
pen.forward(180)
pen.end_fill()

# Hide the turtle and display the card
pen.hideturtle()
screen.mainloop()
