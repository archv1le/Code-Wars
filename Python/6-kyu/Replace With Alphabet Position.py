def alphabet_position(text):
    result = []
    for char in text:
        if char.isalpha():
            result.append(str(ord(char.lower()) - ord('a') + 1))

    return ' '.join(result)
