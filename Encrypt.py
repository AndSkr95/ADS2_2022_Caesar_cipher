import string


class Encrypt:
    def __init__(self, number: int, text: str):
        self.__shift_pattern = number
        self.__plain_text = text
        self.result = ""
        self.encrypt()

    def encrypt(self):
        for i in range(len(self.__plain_text)):
            char = self.__plain_text[i]
            if char.isupper():
                self.result += chr((ord(char) + self.__shift_pattern-65) % 26 + 65)

            elif char.isspace():
                self.result += " "

            else:
                self.result += chr((ord(char) + self.__shift_pattern - 97) % 26 + 97)

        return self.result

