def title_case(title, minor_words=''):
    minor_words = set(minor_words.lower().split())
    
    title = [word.capitalize() if word.lower() not in minor_words or i == 0 else word.lower() for i, word in enumerate(title.split())]
    
    return ' '.join(title)
