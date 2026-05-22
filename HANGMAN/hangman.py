import function_hangman
import hangman_visuals


start = hangman_visuals.hangman_start()
print(start)
user_choice = input("Enter your choice for game toughness (E/M/H) : ")

if (user_choice in ["E","e","M","m","H","h"]) :

     if(user_choice in ["e","E"]) :
          word = "tomato"
          #function_hangman.choice_easy() 
          max_chances = len(word)
          remaining_chances = max_chances
          visual_box = hangman_visuals.draw_hangman(remaining_chances)
          print(visual_box)
          print(f"So You have got {max_chances} guess to find the words \nLet's see who win's your bad luck or my good luck 😁😁🥷 ")
          blank_word =("_" * len(word))
          print(blank_word)
          while True : 
               guess = input(f"Enter the element you guess is right : ")

               blank_word = function_hangman.replace_blank(word,guess,blank_word,remaining_chances)
               print (blank_word)
               remaining_chances = function_hangman.chance_left(remaining_chances)
               visual_box = function_hangman.replace_blank(word,guess,blank_word,remaining_chances)








     elif(user_choice in ["M","m"]) :
          function_hangman.choice_med()




     elif(user_choice in ["H","h"]):
          function_hangman.choice_hard()
     else :
          print("Error 404 ")
else :
     print("Enter A Valid Input My Dear User ")
     