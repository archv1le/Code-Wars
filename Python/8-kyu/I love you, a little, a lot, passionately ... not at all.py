def how_much_i_love_you(nb_petals):
    phrases = ["I love you", "a little", "a lot", "passionately", "madly", "not at all"]
    
    index = (nb_petals - 1) % len(phrases)
    
    return phrases[index]
