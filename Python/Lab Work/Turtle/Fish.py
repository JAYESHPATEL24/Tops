import turtle

vatsal = turtle.Turtle()
vatsal.color('black')
vatsal.screen.bgcolor("#a2a2d0")
vatsal.pensize(10)
 
def Draw_Fish(i, j):
    vatsal.penup()
    vatsal.goto(i, j)
    vatsal.speed(10)
    vatsal.left(45)
    vatsal.pendown()
    vatsal.forward(100)
    vatsal.right(135)
    vatsal.forward(130)
    vatsal.right(130)
    vatsal.forward(90)
    vatsal.left(90)
    vatsal.right(90)
    vatsal.circle(200, 90)
    vatsal.left(90)
    vatsal.circle(200, 90)
    vatsal.penup()
    vatsal.left(130)
    vatsal.forward(200)
    vatsal.pendown()
    vatsal.circle(10, 360)
    vatsal.right(270)
    vatsal.penup()
    vatsal.forward(50)
    vatsal.pendown()
    vatsal.left(90)
    vatsal.circle(100, 45)
    vatsal.penup()
    vatsal.forward(300)
    vatsal.left(135)
    vatsal.pendown()
    vatsal.right(180)
 
Draw_Fish(0, 0)
Draw_Fish(150, 150)
Draw_Fish(150, -150)

turtle.done()