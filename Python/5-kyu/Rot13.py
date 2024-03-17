def rot13(message):
    result = ''
    for char in message:
        if char.isalpha():
            if char.isupper():
                shifted_char = chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
            else:
                shifted_char = chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
            result += shifted_char
        else:
            result += char
    return result
