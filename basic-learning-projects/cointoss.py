import random
# COIN TOSS GAME
print('''-
    ╔══════════════════════════════════════════════╗ 
    ║        WELCOME TO THE COIN TOSS GAME        ║
    ╚══════════════════════════════════════════════╝
      ''')
toss = random.choice(["Heads", "Tails"])
user = input("Enter your choice (Heads/Tails) : ")
if (user == "Heads" or user == "Tails") :
    if toss == user :
        print("Congratulations! You won the toss")
    else :
        print("Better luck next time! Computer won the toss")