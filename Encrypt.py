import string


class Encrypt:
    def __init__(self, number: int, text: str):
        """
        Encrypts a message using Caesar Cipher (Rot(n) not implemented).
        :param number: The number of positions to shift
        :param text: Plain text to encrypt
        """
        self.__shift_pattern = number
        self.__plain_text = text
        self.result = ""
        self.encrypt()

    def encrypt(self):
        """
        Encrypts the message.
        :return:
        """
        for i in range(len(self.__plain_text)):
            char = self.__plain_text[i]
            if char.isupper():
                self.result += chr((ord(char) + self.__shift_pattern-65) % 26 + 65)

            elif char.isspace():
                self.result += " "

            else:
                self.result += chr((ord(char) + self.__shift_pattern - 97) % 26 + 97)



