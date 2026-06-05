import random 
import function as f 
from turtle import Turtle,Screen 
screen = Screen() 
screen.setup(1200,500)
screen.bgcolor('black')
y = [200,110,20,-80,-200]
poke = []
poke_name = ["Darkrai","Cresselia","Lugia","Gardevoir","Umbreon"]
guess = screen.textinput("Let the Pokemons Race", "Which pokemon you think win ?(1,2,3,4,5)")
for i in range(5) :
    pokemon = Turtle()
    pokemon.name = poke_name[i]
    pokemon.speed('normal')
    screen.addshape(f'{i+1}.gif')
    pokemon.penup()
    pokemon.goto(-550,y[i])
    pokemon.shape(f'{i+1}.gif')
    poke.append(pokemon)


## Used ai/chatgpt bcoz logic i was using was unable to stop them once one of the pokemon reached end point
# although winner name through print could be printed  
winner = None

while winner is None:
    choice = random.choice(poke)
    choice.forward(random.randint(10, 15))

    for pokemon in poke:
        if pokemon.xcor() >= 520:
            winner = pokemon
            break

print("Winner is:", winner.name)
screen.exitonclick()
