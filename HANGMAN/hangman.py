import function_hangman
import hangman_visuals
import os

start = hangman_visuals.hangman_start()

print(start)

user_choice = input("Enter your choice for game toughness (E/M/H) : ")
if(user_choice in ["E","e","M","m","H","h"]) :
    if(user_choice in ["e","E"]) :
        word = function_hangman.choice_easy()
    elif(user_choice in ["M","m"]) :
        word = function_hangman.choice_med()
    elif(user_choice in ["H","h"]) :
        word = function_hangman.choice_hard()
    max_chances = 6
    remaining_chances = max_chances
    guessed_letters = []
    
    os.system("cls" if os.name == "nt" else "clear")
    visual_box = hangman_visuals.draw_hangman(remaining_chances)
    print(visual_box)
    print(f"So You have got {max_chances} guess to find the word")
    blank_word = ("_" * len(word))

    print(blank_word)

    while(remaining_chances > 0) :
        guess = input("Enter the element you guess is correct : ").lower()
        
        if(len(guess) != 1 or not guess.isalpha()) :
            os.system("cls" if os.name == "nt" else "clear")
            print(visual_box)
            print("Please Enter a single valid letter !")
            print(blank_word)
            continue
            
        if(guess in guessed_letters) :
            os.system("cls" if os.name == "nt" else "clear")
            print(visual_box)
            print(f"You have already guessed '{guess}' !!")
            print(blank_word)
            continue
            
        guessed_letters.append(guess)
        
        old_blank = blank_word
        blank_word = (function_hangman.replace_blank(word,guess,blank_word))
        
        os.system("cls" if os.name == "nt" else "clear")
        
        if(old_blank == blank_word) :
            remaining_chances = (function_hangman.chance_left(remaining_chances))
            visual_box = (hangman_visuals.draw_hangman(remaining_chances))
            print(visual_box)
            print("Wrong Guess dY~-")
            print(f"You are left with {remaining_chances} chances !!")
        else :
            visual_box = (hangman_visuals.draw_hangman(remaining_chances))
            print(visual_box)
            print("Correct Guess dY~Z")
            print(f"You are left with {remaining_chances} chances !!")
            
        print(blank_word)
        
        if(blank_word == word) :
            print("Congo You Won!!! dYZ%")
            break
        
    if(remaining_chances == 0) :
        print("You Lost dY~-")
        print(f"Word Was : {word} ")
else :

    print("Enter A Valid Input My Dear User")
