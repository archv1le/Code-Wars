def is_pangram(s):
    alphabet_set = set("abcdefghijklmnopqrstuvwxyz")
    cleaned_string = ''.join(char.lower() for char in s if char.isalpha())
    return set(cleaned_string) == alphabet_set
