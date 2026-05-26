from wonderwords import RandomWord 

def choice_easy() :
    r = RandomWord()
    word = r.word(word_min_length = 5 , word_max_length = 7)
    return word

def choice_med() :
    r = RandomWord()
    word = r.word(word_min_length = 7 , word_max_length = 9)
    return word

def choice_hard() :
    r = RandomWord()
    word = r.word(word_min_length = 9 , word_max_length = 11)
    return word

def replace_blank(word,guess,blank_word) :

    for i in range(len(word)) :
        if(guess == word[i]) :
            blank_word = (blank_word[:i] + guess + blank_word[i+1:])

    return blank_word
                
def chance_left(remaining_chances) :
    remaining_chances = remaining_chances - 1
    return remaining_chances    
