import math
from turtle import * 

def hearta(k):
    return 15 * math.sin(k)**3

def heartb(k):
    return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

speed(1)
tracer(2)  
bgcolor("black")


for i in range(800):
    goto(hearta(i)*15,heartb(i)*15)

    for j in range(1):
        color("red")

        hideturtle()
        goto(0,0)
done()