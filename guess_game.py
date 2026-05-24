# Add Ascii art for starting the game here
print(r'''
   _____                          _____                      
  / ____|                        / ____|                     
 | |  __ _   _  ___  ___ __     | |  __   __ _ _ __ ___   ___ 
 | | |_ | | | |/ _ \/ __/ __    | | |_ | / _` | '_ ` _ \ / _ \
 | |__| | |_| |  __/\__ \__ \   | |__| || (_| | | | | | |  __/
  \_____|\__,_|\___||___/___/    \_____| \__,_|_| |_| |_|\___|
                                                          
''')
import random 

count = int(input("Enter the no. of players interested to play the game : "))
computer_choice = random.randint(0,100) 
guess = {}
if(count == 1):
  print("\n------ MAN VS COMPUTER ------")
  name = input("Enter the name of player : ")
  count_guess = int(input("Enter your guess (0-100) : "))
  guess[name] = count_guess
  guess["Computer"] = random.randint(0,100)
else :
  for i in range(0,count) :
      print(f"-----------------PLAYER {i+1}-----------------")
      name = input("Enter the name of player : ")
      count_guess = int(input("Enter your guess (0-100) : "))
      guess[name] = count_guess

target = 0 
minim_value = 100 
for value in guess.values() :
  result = abs(computer_choice - value)
  if (result < minim_value):
    minim_value = result
    target = value

for key,value in guess.items() :
   if(target == value) :
    print(f"\n----------------- RESULT TIME -----------------")
    print (f"\n\nSystem's Choice was {computer_choice}\n{key} got it right with his guess of {value}\n{key} was closest with margin of {minim_value}")
