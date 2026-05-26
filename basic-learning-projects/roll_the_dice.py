import random as r 
import os 
def roll_dice(dice_no) : 
    i = 0
    while (i<dice_no) :
        print(r.choice(dice_face))
        i+=1 

print('''

╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║  ██╗     ███████╗████████╗███████╗    ██████╗ ██╗      █████╗ ██╗   ██╗   ║
║  ██║     ██╔════╝╚══██╔══╝██╔════╝    ██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝   ║
║  ██║     █████╗     ██║   ███████╗    ██████╔╝██║     ███████║ ╚████╔╝    ║
║  ██║     ██╔══╝     ██║   ╚════██║    ██╔═══╝ ██║     ██╔══██║  ╚██╔╝     ║
║  ███████╗███████╗   ██║   ███████║    ██║     ███████╗██║  ██║   ██║      ║
║  ╚══════╝╚══════╝   ╚═╝   ╚══════╝    ╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝      ║
║                                                                           ║
║    ██████╗  ██████╗ ██╗     ██╗        ████████╗██╗  ██╗███████╗    ██████╗ ██╗ ██████╗███████╗  
║    ██╔══██╗██╔═══██╗██║     ██║        ╚══██╔══╝██║  ██║██╔════╝    ██╔══██╗██║██╔════╝██╔════╝  
║    ██████╔╝██║   ██║██║     ██║           ██║   ███████║█████╗      ██║  ██║██║██║     █████╗    
║    ██╔══██╗██║   ██║██║     ██║           ██║   ██╔══██║██╔══╝      ██║  ██║██║██║     ██╔══╝    
║    ██║  ██║╚██████╔╝███████╗███████╗      ██║   ██║  ██║███████╗    ██████╔╝██║╚██████╗███████╗  
║    ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝      ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═════╝ ╚═╝ ╚═════╝╚══════╝  
║                              _______                                              ║
║                             /\ o o o\                                             ║
║                            /o \ o o o\_______                                     ║
║                           <    >------>   o /|                                    ║
║                            \ o/  o   /_____/o|                                    ║ 
║                             \/______/     |oo|                                    ║
║                                   |   o   |o/                                     ║
║                                   |_______|/                                      ║
║                                                                                   ║
╚═══════════════════════════════════════════════════════════════════════════════════╝
      ''')

face1 = ('''┌─────────┐  
│         │ 
│    ●    │ 
│         │ 
└─────────┘''')
face2 = ('''┌─────────┐
│  ●      │
│         │
│      ●  │
└─────────┘''')
face3 = ('''┌─────────┐
│  ●      │
│    ●    │
│      ●  │
└─────────┘''')
face4 = ('''┌─────────┐
│  ●   ●  │
│         │
│  ●   ●  │
└─────────┘''')
face5 = ('''┌─────────┐
│  ●   ●  │
│    ●    │
│  ●   ●  │
└─────────┘''')
face6 = ('''┌─────────┐
│  ●   ●  │
│  ●   ●  │
│  ●   ●  │
└─────────┘''')

dice_face = [face1,face2,face3,face4,face5,face6]
dice_no = int(input("Number of Dice you need for your game(Enter 0 to Quit) : "))
if (dice_no == 0 ) :
    print("Game Closed 🎲")


else : 
    roll_dice(dice_no)
    while True : 
        choice = input("Do You Want to Roll Again(y/n): ")
        os.system('cls') 
        if(choice in ["y","Y","n","N"]) :
            if (choice in ["y","Y"]) :
                roll_dice(dice_no)
            else :
                print("User Stopped the DICE roll")
                break
        else :
            print("Please Enter a Valid Response")

# horizontal stacking of dice could have been a better solution for user expericence and display window space occupancy but i was facing issue in that and unable to complete
# that on my own may be later i will get that athough i got solution that from ai tools but i belive as i am learing i should learn on my own but can keep those things 
# in my mind for next time to improve future works

"""
import random as r

# Beautiful title banner from trail.py
print(r'''
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║  ██╗     ███████╗████████╗███████╗    ██████╗ ██╗      █████╗ ██╗   ██╗   ║
║  ██║     ██╔════╝╚══██╔══╝██╔════╝    ██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝   ║
║  ██║     █████╗     ██║   ███████╗    ██████╔╝██║     ███████║ ╚████╔╝    ║
║  ██║     ██╔══╝     ██║   ╚════██║    ██╔═══╝ ██║     ██╔══██║  ╚██╔╝     ║
║  ███████╗███████╗   ██║   ███████║    ██║     ███████╗██║  ██║   ██║      ║
║  ╚══════╝╚══════╝   ╚═╝   ╚══════╝    ╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝      ║
║                                                                           ║
║    ██████╗  ██████╗ ██╗     ██╗        ████████╗██╗  ██╗███████╗    ██████╗ ██╗ ██████╗███████╗  
║    ██╔══██╗██╔═══██╗██║     ██║        ╚══██╔══╝██║  ██║██╔════╝    ██╔══██╗██║██╔════╝██╔════╝  
║    ██████╔╝██║   ██║██║     ██║           ██║   ███████║█████╗      ██║  ██║██║██║     █████╗    
║    ██╔══██╗██║   ██║██║     ██║           ██║   ██╔══██║██╔══╝      ██║  ██║██║██║     ██╔══╝    
║    ██║  ██║╚██████╔╝███████╗███████╗      ██║   ██║  ██║███████╗    ██████╔╝██║╚██████╗███████╗  
║    ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝      ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═════╝ ╚═╝ ╚═════╝╚══════╝  
║                              _______                                              ║
║                             /\ o o o\                                             ║
║                            /o \ o o o\_______                                     ║
║                           <    >------>   o /|                                    ║
║                            \ o/  o   /_____/o|                                    ║ 
║                             \/______/     |oo|                                    ║
║                                   |   o   |o/                                     ║
║                                   |_______|/                                      ║
║                                                                                   ║
╚═══════════════════════════════════════════════════════════════════════════════════╝
''')

# Dice faces split into lists of rows (from try.py) to support side-by-side printing
face1 = [
    "┌─────────┐",
    "│         │",
    "│    ●    │",
    "│         │",
    "└─────────┘"
]

face2 = [
    "┌─────────┐",
    "│  ●      │",
    "│         │",
    "│      ●  │",
    "└─────────┘"
]

face3 = [
    "┌─────────┐",
    "│  ●      │",
    "│    ●    │",
    "│      ●  │",
    "└─────────┘"
]

face4 = [
    "┌─────────┐",
    "│  ●   ●  │",
    "│         │",
    "│  ●   ●  │",
    "└─────────┘"
]

face5 = [
    "┌─────────┐",
    "│  ●   ●  │",
    "│    ●    │",
    "│  ●   ●  │",
    "└─────────┘"
]

face6 = [
    "┌─────────┐",
    "│  ●   ●  │",
    "│  ●   ●  │",
    "│  ●   ●  │",
    "└─────────┘"
]

dice_faces = [face1, face2, face3, face4, face5, face6]

def roll_dice(dice_no):
    # Roll the specified number of dice
    rolled = [r.choice(dice_faces) for _ in range(dice_no)]
    print("\nRolling...\n")
    
    # Print the dice side-by-side row by row (logic from try.py)
    for row in range(5):
        for die in rolled:
            print(die[row], end="  ")
        print()
    print()

while True:
    # Outer loop to start the game or change number of dice
    try:
        dice_no = int(input("Number of Dice you need for your game (Enter 0 to Quit): "))
    except ValueError:
        print("Please enter a valid integer.")
        continue

    if dice_no == 0:
        print("Game Closed 🎲")
        break
    
    # Initial roll
    roll_dice(dice_no)
    
    # Inner loop for rolling the same quantity again
    while True:
        choice = input("Do You Want to Roll Again (y/n): ").strip().lower()
        if choice in ["y", "yes"]:
            roll_dice(dice_no)
        elif choice in ["n", "no"]:
            print("User stopped the DICE roll\n")
            break
        else:
            print("Please Enter a Valid Response")
"""