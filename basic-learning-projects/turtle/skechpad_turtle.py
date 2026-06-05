import random as r 
from turtle import Turtle , Screen
screen = Screen()
t = Turtle()
t.speed('fastest')

# pen_down = True 
def draw_square() :
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)    
    #t.left(180)
def move_fwd() :
    t.seth(0)
    t.fd(20)
def move_bck() :
    t.seth(180)
    t.fd(20)
def move_up() :
    t.seth(90)
    t.fd(20)
def move_down() : 
    t.seth(270)
    t.fd(20)
def turn_left() :
    t.left(10)
def turn_right() :
    t.right(10)
def move() :
    t.fd(10)
def change_pen():
    global pen_down
    pen_down = not pen_down
    if pen_down:
        t.pendown()
    else:
        t.penup()

screen.listen()


# screen.onkeypress(move, "w")
# screen.onkeypress(turn_left, "a")
# screen.onkeypress(turn_right, "d")
# screen.onkey(change_pen, 'space')

screen.onkeypress(move_bck, "a")
screen.onkeypress(move_down, "s")
screen.onkeypress(move_up, "w")
screen.onkeypress(move_fwd, "d")

screen.onkeypress (move_up, "Up")
screen.onkeypress(move_down, "Down")
screen.onkeypress(move_bck, "Left")
screen.onkeypress(move_fwd, "Right")
screen.exitonclick()