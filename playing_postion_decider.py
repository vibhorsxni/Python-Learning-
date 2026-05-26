import random

print('''
      ╔══════════════════════════════════════════════╗
      ║      SPORTS PLAYING POSITION DECIDER         ║
      ╚══════════════════════════════════════════════╝
      ''')

permission = input("Do you want to enter the game name ? (Y/N) : ")

game = "game"

if permission == "Y" or permission == "y" :

    game = input("Enter the name of the game you want to play : ")
    print(f"{game}")

elif permission == "N" or permission == "n" :
    print("No Problem")

else :
    print("No Problem")

n = int(input(f"Enter the number of person playing the {game} : "))
name = []

for i in range(n) :
    name.append(input("Enter the name of the player : "))

print ("------------PLAYING ORDER FOR PLAYERS IS AS FOLLOWS------------\n")
player_first = 0 
for i in range(n) :
    player_first = random.choice(name)
    print(f"               {i+1} - Position = {player_first}")
    name.remove(player_first)



