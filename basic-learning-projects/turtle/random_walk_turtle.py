import random as r 
from turtle import Turtle , Screen
screen = Screen()
screen.colormode(255)
t = Turtle()

x = int(screen.textinput('Enter the Value','Enter the no. of step counts : '))
t.shape('turtle')
t.speed('fastest')
t.pensize(2)

screen.bgcolor('black')
screen.addshape('pokemon.gif')
t.shape('pokemon.gif')

for i in range(x) :
    t.color(r.randint(0,255),r.randint(0,255),r.randint(0,255))
    choice = r.choice([-20,20])
    angle = [-90,90,180,-180]
    turn = r.choice(angle)

    t.forward(choice)
    t.seth(turn)


screen.exitonclick()