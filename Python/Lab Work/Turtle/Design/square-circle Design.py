from turtle import *

speed(0)
bgcolor("black")
pencolor("orange")

def square(x,y):
    for j in range(4):
        forward(x)
        right(y)

for i in range(80):
    square(170,90)
    right(5)
    circle(50)
    right(50)
    hideturtle()

done()