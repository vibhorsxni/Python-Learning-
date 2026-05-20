#  find treasure -

import random as r
print ('''          ╔══════════════════════════════════════════════╗ 
          ║        WELCOME TO THE TREASURE GUESS         ║
          ╚══════════════════════════════════════════════╝''')
# ALGO 
# ENTER MATRIX SIZE USER WANT -> EX - AXB       - DONE 
# PRINT NO OF CHANCES USER WILL GET TO FIND THE TREASURE        - DONE
# PRINT THE MATRIX BOX IN AXB FORMAT  - DONE
# TAKE INPUT OF USER GUESS IN THE FORM OF ROW NUMBER AND COLUMN NUMBER OR CO -ORDINATES - DONE
# CHECK IF USER GUESS IS CORRECT OR NOT -done 
# REVEAL THE TREASURE BOX IF USER GUESS IS CORRECT -done 
# AND CHANCE-- -done 
# ELSE - WRONG ANOTHER GUESS WITH TREASURE BOX SHUFFLED AGAIN -done  
#REPEAT TILL CHANCE == 0 OR USER GUESS IS CORRECT - done 
# IF WON  - done 
# PRINT CONGRATS - done 
# PRINT MATRIX WITH TREASURE BOX REVEALED - done



#----------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------


# matrix size input from user 
rows = int(input("Enter the number of rows you want in the matrix : "))
if rows < 0  :
    print("Invalid Format!)")
cols = int(input("Enter the number of columns you want in the matrix : "))
if cols < 0 :
    print("Invalid Format!)")

# choose random co-ordinates for the treasure box
treasure_row = r.randint(1,rows)
treasure_col = r.randint(1,cols)
a = (treasure_row, treasure_col)

# assigning no. possible chances user has to find the treasure box
chances = 0 
if rows == cols :
    chances = rows
elif rows > cols :
    chances = cols
else : 
    chances = rows
print("\n")
print(f"🥸 You will get {chances} to guess the treasure box") 


# print the matrix box in AXB format
for i in range(rows) :
    print("       ")
    for j in range(cols) :
        print("       ",end = " ")
        print(f"🏦", end = " ")
    print("\n")   


wrong_guess = []
# take input of user guess in the form of row number and column number or co-ordinates
while chances > 0 :
    row_guess = int(input("Enter the row number which you chose : "))
    if row_guess >rows :
        print("Invalid input! Please enter valid co-ordinates")
        continue
    column_guess = int(input("Enter the column number which you chose : "))
    if  column_guess > cols :
        print("Invalid input! Please enter valid co-ordinates")
        continue

# check if user guess is correct or not
    if row_guess == treasure_row and column_guess == treasure_col :
        print("Congratulations! You found the treasure box 🥳\n")
        for i in range(rows) :
            print("       ")
            for j in range(cols) :
                if i == treasure_row - 1 and j == treasure_col - 1 :
                    print("       ",end = " ")
                    print(f"🪙", end = " ")
                else :
                    print("       ",end = " ")
                    print(f"🏦", end = " ")
            print("\n")   
        
        break
    else :
        wrong_guess.append((row_guess, column_guess))
        for i in range(rows) :
            print("       ")
            for j in range(cols) :
                if (i + 1, j + 1) in wrong_guess:
                    print("       ",end = " ")
                    print(f"❌", end = " ")
                else :
                    print("       ",end = " ")
                    print(f"🏦", end = " ")
            print("\n")
        if chances - 1 > 0 :
            print("Wrong guess!, Hard Luck")
            print(f"Don't worry! Dear you still have {chances -1 } chances left to find the treasure box")
        else :
            print("Wrong guess!, Hard Luck")
    chances -= 1
while chances == 0 :
    print("Better luck next time! You cou ldn't find the treasure box")
    print(f"The treasure box was in row {treasure_row} and column {treasure_col}")
    for i in range(rows) :
        print("       ")
        for j in range(cols) :
            if i == treasure_row - 1 and j == treasure_col - 1 :
                print("       ",end = " ")
                print(f"🪙", end = " ")
            elif (i + 1, j + 1) in wrong_guess:
                print("       ",end = " ")
                print("❌", end=" ")
            else :
                print("       ",end = " ")
                print(f"🏦", end = " ")
        print("\n")
    break 
