def position(alphabet):
    alphabet = alphabet.lower()
    
    position = ord(alphabet) - ord('a') + 1
    
    return "Position of alphabet: " + str(position)
