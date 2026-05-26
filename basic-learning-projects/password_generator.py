
#  secrets could have been used in place of random for better security purpose as random uses mathematical algorithm
#  for various operation of choosing and shuffling while secrets has better security operation as compared to the random as it takes info
#  and Uses your operating system's secure randomness based on system events (timing, hardware randomness, system state, etc.).

import random as r
import string 

print (r"""
 ____                                     _       ____                           _             
|  _ \ __ _ ___ _____      _____  _ __ __| |     / ___| ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
| |_) / _` / __/ __\ \ /\ / / _ \| '__/ _` |    | |  _ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
|  __/ (_| \__ \__\ \ V  V / (_) | | | (_| |    | |_| |  __/ | | |  __/ | | (_| | || (_) | | 
|_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_|     \____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
 
""")

choice = input("Do you want to choose the alphabets,integers and special characters for your password (y/n) : ")
print("\n")

if choice == "y" or choice == "Y" or choice == "n" or choice == "N" : 
    user_choice = []
    password = []
    if choice == "y" or choice == "Y" :
        alphabets = input("Enter the alphabets you need in password(without space and any symbol) : ")
        user_choice.append(alphabets)
        integer = (input("Enter the integers you need in password(without space and any symbol) : "))
        user_choice.append(integer)
        special_character = input("Enter the special characters you need in password(without space and any symbol) : ")
        user_choice.append(special_character)
       
        for i in user_choice :
            password.extend(i)
        r.shuffle(password)
        password = ''.join(password)
        print("\n")
        print(f"Gentleman here is the password generated from your provided data set :-  {password}\n")
        print(f"------------------------------{password}------------------------------\n")
        
    elif choice == "n" or choice == "N" : 
        alphabets = int(input("Enter the no of alphabets you need in password : "))
        user_choice.append(r.choices(string.ascii_letters, k= alphabets))
        integer = int(input("Enter the no of integers you need in password : "))
        user_choice.append(r.choices(string.digits, k= integer))
        special_character = int(input("Enter the no of special characters you need in password : "))
        user_choice.append(r.choices(string.punctuation, k = special_character))
        for i in user_choice :
            password.extend(i)
        r.shuffle(password)
        password = ''.join(password)
        print("\n")
        print(f"Gentleman here is the password generated from radomised data set :-  {password}\n")
        print(f"------------------------------{password}------------------------------\n")
else :
    print (f"Enter a valid input")