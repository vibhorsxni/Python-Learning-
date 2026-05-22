import function_hangman
import hangman_visuals

start = hangman_visuals.hangman_start()
print(start)

user_choice = input("Enter your choice for game toughness (E/M/H) : ")

if user_choice in ["E","e","M","m","H","h"]:

    if user_choice in ["E","e"] :
        word = function_hangman.choice_easy()

    elif user_choice in ["M","m"]:
        word = function_hangman.choice_med()
    else:
        word = function_hangman.choice_hard()
    max_chances = len(word)
    remaining_chances = max_chances
    blank_word = "_" * len(word)
    print(f"So You have got {max_chances} guess to find the word\nLet's see who wins 😁😁🥷")
    while remaining_chances > 0:
        print(blank_word)
        guess = input("Enter the element you guess is right : ").lower()
        old_blank = blank_word
        blank_word = function_hangman.replace_blank(word,guess,blank_word)
        if old_blank == blank_word:

            remaining_chances -= 1
            print(hangman_visuals.draw_hangman(remaining_chances))
            print(f"Wrong Guess! {remaining_chances} left")

        if blank_word == word:

            print("Congo You Won!!! 🎉")
            break

    else:
        print("You Lost 😭")
        print("Word was :", word)