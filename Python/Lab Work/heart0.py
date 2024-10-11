import math
from turtle import *

def hearta(k):
    return 15 * math.sin(k)**3

def heartb(k):
    return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

speed(0)
tracer(0, 0)  # Turn off animation
bgcolor("black")
color("red")
begin_fill()

for i in range(1000):  # Reduce the number of iterations
    k = i * 0.01  # Adjust the increment for smoother drawing
    x = hearta(k) * 20
    y = heartb(k) * 20
    goto(x, y)

end_fill()
color("white")
penup()
goto(0, -20)  # Move to the position to write the text
pendown()
write("I love you", align="center", font=("Arial", 12, "bold"))

hideturtle()
update()  # Update the drawing
done()
