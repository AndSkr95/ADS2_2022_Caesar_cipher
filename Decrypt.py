import string


class Decrypt:
    def __init__(self, shift_pattern: int, message: str):
        """
        Decrypts a Caesar Cipher message (Rot(n) not implemented).
        :param shift_pattern: the number of positions to shift.
        :param message: Encrypted message to decrypt
        """
        self._shift_pattern = shift_pattern
        self._encrypted_message = message
        self.result = ""
        self.decrypt()

    def decrypt(self):
        alphabet = string.ascii_letters
        print(alphabet)

        for i in range(len(self._encrypted_message)):
            char = self._encrypted_message[i]
            if char in alphabet:
                position = alphabet.find(char)
                new_pos = (position - self._shift_pattern) % 26
                new_char = alphabet[new_pos]
                self.result += new_char
            else:
                self.result += char

