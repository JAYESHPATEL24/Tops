import turtle

# Function to draw a rose
def draw_rose(t, x, y, size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("red", "pink")
    t.begin_fill()
    for _ in range(36):  # Draw petals
        t.circle(size, 60)
        t.left(120)
        t.circle(size, 60)
        t.left(10)
    t.end_fill()
    
    # Draw the center of the rose
    t.penup()
    t.goto(x , y + size * (-0.2))  # Adjust position for the center to the left and down
    t.pendown()
    t.color("yellow")
    t.begin_fill()
    t.circle(size // 5)
    t.end_fill()

# Set up the screen
screen = turtle.Screen()
screen.title("Thank You Card")
screen.bgcolor("lightblue")

# Create a turtle object
pen = turtle.Turtle()
pen.speed(2)
pen.color("blue")

# Draw roses first
pen.speed(0)
draw_rose(pen, -200, 200, 50)  # Upper-left corner
draw_rose(pen, 200, 200, 50)   # Upper-right corner
draw_rose(pen, -200, -200, 50) # Lower-left corner
draw_rose(pen, 200, -200, 50)  # Lower-right corner

# Write the gratitude message
pen.color("blue")
pen.speed(1)
pen.penup()
pen.goto(0, 150)
pen.pendown()
pen.write("Thank You!", align="center", font=("Arial", 40, "bold"))

pen.penup()
pen.goto(0, 50)
pen.pendown()
pen.write("For Being an Amazing Soft Skill Teacher", align="center", font=("Arial", 20, "normal"))

# Draw a heart
pen.color("purple")
pen.penup()
pen.goto(0, -200)
pen.pendown()
pen.speed(1)

pen.begin_fill()
pen.left(140)
pen.forward(120)
pen.circle(-60, 200)
pen.left(120)
pen.circle(-60, 200)
pen.forward(120)
pen.end_fill()

# Hide the turtle and display the card
pen.hideturtle()
screen.mainloop()
