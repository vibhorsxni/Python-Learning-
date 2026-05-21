from wonderwords import RandomWord 
def choice_easy() :
    r = RandomWord()
    word = r.word(word_min_length = 5 , word_max_length = 7)
    return word

