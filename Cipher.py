from collections import Counter


# Базовый класс шифра
class Cipher:
    MAX = 2 ** 16

    def __init__(self, key):
        self.key = key

    # Преобразование в из ord в char
    @staticmethod
    def get_chars(ords):
        return list(map(chr, ords))

    # Преобразование в из char в ord
    @staticmethod
    def get_ords(chars):
        return list(map(ord, chars))


# Шифр Цезаря
class Caesar(Cipher):
    MAX = 2 ** 16 - 1

    def __init__(self, key):
        super().__init__(key)

    def encrypt(self, text):
        return "".join(self.get_chars([(char + self.key) % self.MAX for char in self.get_ords(text)]))

    def invert_key(self):
        self.key = -self.key

    def decrypt(self, text, key=True):
        if key:
            self.invert_key()
            result = self.encrypt(text)
            self.invert_key()
            return result
        else:
            return "".join(self.get_chars([(char - key) % self.MAX for char in self.get_ords(text)]))

    # Находится самый часто употребляемый символ
    # и рассматривается как символ пробела
    # и относительно этого дешифруется текст
    def hack(self, text):
        most_common = Counter(text).most_common()[0][0]
        key = ord(most_common) - ord(' ')
        return self.decrypt(text, key)


# Шифр Вернама
class Vernam(Cipher):
    def __init__(self, key):
        super().__init__(key)

    def encrypt(self, text):
        return "".join(self.get_chars([char ^ self.key for char in self.get_ords(text)]))

    def decrypt(self, text):
        return self.encrypt(text)
