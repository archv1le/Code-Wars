def add_length(str_):
    words = str_.split()
    
    result = [f"{word} {len(word)}" for word in words]
    
    return result
