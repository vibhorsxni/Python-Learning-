import random 
from turtle import Turtle,Screen 

screen = Screen()

def poke_1() :
    pokemon_1 = Turtle()
    pokemon_1.speed('normal')
    screen.addshape('1.gif')
    pokemon_1.penup()
    pokemon_1.goto(-500,200)
    pokemon_1.shape('1.gif')
    return pokemon_1

def poke_2() :
    pokemon_2 = Turtle()
    pokemon_2.speed('normal')
    pokemon_2.penup() 
    pokemon_2.goto(-500,110)
    screen.addshape('2.gif')
    pokemon_2.shape('2.gif')
    return pokemon_2

def poke_3() :
    pokemon_3 = Turtle()
    pokemon_3.speed('normal')
    pokemon_3.penup() 
    pokemon_3.goto(-500,20)
    screen.addshape('3.gif')
    pokemon_3.shape('3.gif')
    return pokemon_3

def poke_4() :
    pokemon_4 = Turtle()
    pokemon_4.speed('normal')
    pokemon_4.penup() 
    pokemon_4.goto(-500,-80)
    screen.addshape('4.gif')
    pokemon_4.shape('4.gif')
    return pokemon_4

def poke_5() :
    pokemon_5 = Turtle()
    pokemon_5.speed('normal')
    pokemon_5.penup() 
    pokemon_5.goto(-500,-200)
    screen.addshape('5.gif')
    pokemon_5.shape('5.gif')
    return pokemon_5

def movement() :
    x = random.choice([poke_1,poke_2,poke_3,poke_4,poke_5])
    while True :
        x.fd(random.randint(20,50))
