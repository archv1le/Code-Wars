def capitals(word):
    return [index for index, char in enumerate(word) if char.isupper()]
