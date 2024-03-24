def duplicate_count(text):
    text_lower = text.lower()
    char_count = {}
    duplicate_count = 0
    
    for char in text_lower:
        char_count[char] = char_count.get(char, 0) + 1
    
    for count in char_count.values():
        if count > 1:
            duplicate_count += 1
    
    return duplicate_count
