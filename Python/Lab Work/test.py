import turtle
from pygame import mixer

# Adding music is optional as per your choice.
# Initialize pygame mixer
mixer.pre_init(frequency=48000, size=-16, channels=2, buffer=512)
mixer.init()
mixer.music.load("C:\\Users\\jayes\\Documents\\Tops\\DF\\new-year-128535.mp3") #add your music file name or path


screen = turtle.Screen()

screen.bgcolor('#000')
screen.title("Saal Mubarak everyone")
screen.screensize(800,800)

mixer.music.play()


firework = turtle.Turtle()
firework.pensize(3)
firework.shape('turtle')
size = 20
firework.stamp
firework.speed(11)
firework.left(90)

firework.color("#EA2027")
for step in range(40):
    firework.forward(100)
    firework.left(180)
    firework.forward(100)
    firework.left(9)

firework.color('#EE5A2A')
for step in range(36):
    firework.forward(130)
    firework.left(180)
    firework.forward(130)
    firework.left(10)

firework.color('#F79F1F')
for step in range(20):
    firework.forward(150)
    firework.left(180)
    firework.forward(150)
    firework.left(18)

firework.color('#3ae374')
for stamps in range(12):
    firework.penup()
    firework.forward(170)
    firework.pendown()
    firework.forward(10)
    firework.penup()
    firework.forward(10)
    firework.stamp()
    firework.right(30)
    firework.penup()
    firework.setpos(0,0)


text = turtle.Turtle()
text.color("#fff")
text.penup()
text.setpos(0,-250)
text.write("\nSaal Mubarak to you and your family....", True, align="center", font=("Monsterrat", 20, "normal"))
text.setpos(0,-270)

screen.mainloop()