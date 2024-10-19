import turtle
import time

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
    t.goto(x, y + size * (-0.2))  # Adjust position for the center to the left and down
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

# Write the gratitude message word by word
pen.color("blue")
pen.speed(1)
pen.penup()
pen.goto(0, 150)
pen.pendown()

message1 = "Thank You!"
message2 = "For Being an Amazing Soft Skill Teacher"
words1 = message1.split()
words2 = message2.split()

# Write the first line word by word
pen.penup()
pen.goto(-len(message1)*5, 150)  # Adjust starting position for better alignment
pen.pendown()
for word in words1:
    pen.write(word + " ", align="left", font=("Arial", 40, "bold"))
    pen.penup()
    pen.forward(80)  # Move turtle forward to space out words
    pen.pendown()
    time.sleep(0.5)  # Adjust the delay as needed

pen.penup()
pen.goto(-len(message2)*5, 50)  # Adjust starting position for better alignment
pen.pendown()

# Write the second line word by word
for word in words2:
    pen.write(word + " ", align="left", font=("Arial", 20, "normal"))
    pen.penup()
    pen.forward(50)  # Move turtle forward to space out words
    pen.pendown()
    time.sleep(0.5)  # Adjust the delay as needed

# Draw a heart at the bottom of the text
pen.color("purple")
pen.penup()
pen.goto(0, -200)  # Adjusted position to be below the text
pen.pendown()
pen.speed(1)
pen.begin_fill()
pen.left(140)
pen.forward(120)  # Reduced size
pen.circle(-60, 200)  # Reduced size
pen.left(120)
pen.circle(-60, 200)  # Reduced size
pen.forward(120)  # Reduced size
pen.end_fill()

# Hide the turtle and display the card
pen.hideturtle()
screen.mainloop()
