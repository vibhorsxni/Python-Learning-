print('''-
      ╔══════════════════════════════════════════════╗
      ║        ROCK • PAPER • SCISSORS GAME         ║
      ╚══════════════════════════════════════════════╝
     ''')
import random 
game_console = r"""
      _=====_                               _=====_
     / _____ \                             / _____ \
   +.-'_____'-.---------------------------.-'_____'-.+
  /   |     |  '.        S O N Y        .'  |  _  |   \
 / ___| /|\ |___ \                     / ___| /_\ |___ \
/ |      |      | ;      ___          ; | _         _ | ;
| | <---   ---> | |     |___|         | ||_|       (_)| |
| |___   |   ___| ;  SELECT   START   ; |___       ___| ;
|\    | \|/ |    /  _     ___      _   \    | (X) |    /|
| \   |_____|  .','" "', |___|  ,'" "', '.  |_____|  .' |
|  '-.______.-' /       \ANALOG/       \  '-._____.-'   |
|               |       |------|       |                |
|              /\       /      \       /\               |
|             /  '.___.'        '.___.'  \              |
|            /                            \             |
 \          /                              \           /
  \________/                                \_________/
"""
print(game_console) 
choice = random.choice(["Rock", "Paper", "Scissors"])
ascii_art = {
    "Rock": """
     _______
 ---'   ____)
       (_____)
       (_____)
       (____)
 ---.__(___)
     ROCK
""",

    "Paper": """
      _______
 ---'    ____)____
            ______)
            _______)
           _______)
 ---.__________)
      PAPER
""",

    "Scissors": """
     _______
 ---'   ____)____
           ______)
        __________)
       (____)
 ---.__(___)
     SCISSORS
"""
}
user = input("Enter your choice (Rock/Paper/Scissors) : ")
if (user == "Rock" or user == "Paper" or user == "Scissors") :

    if (user == choice) :
        print (f"{ascii_art[user]} VS {ascii_art[choice]}")
        print("It's a tie !")

    #Winning Situations
    else :     
        if (user == "Rock" and choice == "Scissors") :
            print (f"{ascii_art[user]} VS {ascii_art[choice]}")
            print (f"Rock Smashes Scissors !")
            print("Congratulations ! You win !")
        elif (user == "Paper" and choice == "Rock") :
            print (f"{ascii_art[user]} VS {ascii_art[choice]}")
            print (f"Paper Covers Rock !")
            print ("Congratulations ! You win !")
        elif (user == "Scissors" and choice == "Paper") :
            print (f"{ascii_art[user]} VS {ascii_art[choice]}")
            print (f"Scissors Cuts Paper !")
            print ("Congratulations ! You win !")

        #Losing Situations

        else :
         if(user == "Rock" and choice == "Paper") :
            print (f"{ascii_art[user]} VS {ascii_art[choice]}")
            print (f"Paper Covers Rock !")
            print("Sorry ! You lose !")
         elif (user == "Paper" and choice == "Scissors") :
            print (f"{ascii_art[user]} VS {ascii_art[choice]}")
            print(f"Scissors Cuts Paper !")
            print("Sorry ! You lose !")
         elif (user == "Scissors" and choice == "Rock") :
            print (f"{ascii_art[user]} VS {ascii_art[choice]}")
            print(f"Rock Smashes Scissors !")
            print("Sorry ! You lose !")
         else :
            print("Please enter a valid choice from the menu")
    print(f"Computer chose : {choice}")
    print("Thanks for playing !, Hope you enjoyed the game !")

    print ('''
███╗   ███╗ █████╗ ██████╗ ███████╗    ██╗    ██╗██╗████████╗██╗  ██╗    ██╗      ██████╗ ██╗   ██╗███████╗
████╗ ████║██╔══██╗██╔══██╗██╔════╝    ██║    ██║██║╚══██╔══╝██║  ██║    ██║     ██╔═══██╗██║   ██║██╔════╝
██╔████╔██║███████║██║  ██║█████╗      ██║ █╗ ██║██║   ██║   ███████║    ██║     ██║   ██║██║   ██║█████╗
██║╚██╔╝██║██╔══██║██║  ██║██╔══╝      ██║███╗██║██║   ██║   ██╔══██║    ██║     ██║   ██║╚██╗ ██╔╝██╔══╝
██║ ╚═╝ ██║██║  ██║██████╔╝███████╗    ╚███╔███╔╝██║   ██║   ██║  ██║    ███████╗╚██████╔╝ ╚████╔╝ ███████╗
╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝     ╚══╝╚══╝ ╚═╝   ╚═╝   ╚═╝  ╚═╝    ╚══════╝ ╚═════╝   ╚═══╝  ╚══════╝


        ♥♥♥       ♥♥♥         ██████╗ ██╗   ██╗    ██╗   ██╗ ██╗ ██████╗  ██╗  ██╗         ♥♥♥       ♥♥♥  
      ♥█████♥   ♥█████♥       ██╔══██╗╚██╗ ██╔╝    ██║   ██║ ██║ ██╔══██╗ ╚██╗██╔╝       ♥█████♥   ♥█████♥       
     ♥███████♥ ♥███████♥      ██████╔╝ ╚████╔╝     ██║   ██║ ██║ ██████╔╝  ╚███╔╝       ♥███████♥ ♥███████♥  
      ♥███████████████♥       ██╔══██╗  ╚██╔╝      ╚██╗ ██╔╝ ██║ ██╔══██╗  ██╔██╗        ♥███████████████♥ 
        ♥███████████♥         ██████╔╝   ██║        ╚████╔╝  ██║ ██████╔╝ ██╔╝ ██╗         ♥███████████♥
          ♥████████♥           ╚═════╝    ╚═╝         ╚═══╝  ╚═╝ ╚═════╝  ╚═╝  ╚═╝           ♥████████♥ 
            ♥████♥                                                                             ♥████♥
              ♥♥                                                                                 ♥♥ 
               
           ''')

else : 
    print("Please enter a valid choice from the menu")

