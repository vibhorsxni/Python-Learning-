import random as r 
from turtle import Turtle , Screen
screen = Screen()
screen.colormode(255)
t = Turtle()
x = int(input(f"Enter the walk step count : "))
t.shape('turtle')
t.speed('fastest')
t.pensize(2)

for i in range(x) :
    t.color(r.randint(0,255),r.randint(0,255),r.randint(0,255))
    choice = r.choice([-20,20])
    angle = [-90,90,180,-180]
    turn = r.choice(angle)

    t.forward(choice)
    t.seth(turn)


screen.exitonclick()