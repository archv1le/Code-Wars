class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet

    def encode(self, text):
        encoded_text = ""
        key_length = len(self.key)
        alphabet_length = len(self.alphabet)

        for i, char in enumerate(text):
            if char in self.alphabet:
                key_char = self.key[i % key_length]
                shift = self.alphabet.index(key_char)
                encoded_char_index = (self.alphabet.index(char) + shift) % alphabet_length
                encoded_char = self.alphabet[encoded_char_index]
                encoded_text += encoded_char
            else:
                encoded_text += char

        return encoded_text

    def decode(self, text):
        decoded_text = ""
        key_length = len(self.key)
        alphabet_length = len(self.alphabet)

        for i, char in enumerate(text):
            if char in self.alphabet:
                key_char = self.key[i % key_length]
                shift = self.alphabet.index(key_char)
                decoded_char_index = (self.alphabet.index(char) - shift) % alphabet_length
                decoded_char = self.alphabet[decoded_char_index]
                decoded_text += decoded_char
            else:
                decoded_text += char

        return decoded_text
