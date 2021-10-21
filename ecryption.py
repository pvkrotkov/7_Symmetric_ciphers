'''''
Написать функцию шифрования и дешифрования текста обобщенным шифром Цезаря.
Написать функцию, принимающую шифротекст, зашифрованный шифром из предыдущего задания и восстанавливающий текст, без знания ключа.
Реализовать в виде функций с.
'''''

import random
import re
class Caesar:
    def __init__(self, key):
        self.key = key
        self.ord_first_letter_lower = ord('а')
        self.ord_first_letter_upper = ord('А')
        self.alphabet_lower = 'йцукенгшщзхъфывапролджэячсмитьбю'
        self.alphabet_upper = self.alphabet_lower.upper()

    def encrypt(self, text) -> str:
        cipher = ''
        for i in text:
            if i in self.alphabet_lower:
                cipher += chr(((ord(i) - self.ord_first_letter_lower + self.key) % 32) + self.ord_first_letter_lower)
            elif i in self.alphabet_upper:
                cipher += chr(((ord(i) - self.ord_first_letter_upper + self.key) % 32) + self.ord_first_letter_upper)
            else:
                cipher += i

        return cipher


    def decrypt_within(self, text) -> str:
        res = []
        for i in range(32):
            res.append(self.decrypt(text, i))
            # new_r = re.sub(r'[^\w\s]', '', res[0])
            print(res[0])
            msg = input('Если Вы можете прочесть этот текст, нажмите на любой символ, иначе - Enter ')
            if msg:
                result = '\n'.join(res)
                return result
            # for j in new_r.split(' '):
            #     if j.lower() in dictionary:
            #         result = '\n'.join(res)
            #         return result
            # if bool(set(dictionary) & set(res)):
            res = []
        return 'Не удалось расшифровать сообщение %s' % text


    def decrypt(self, text, j = -1) -> str:
        cipher = ''
        if j != -1:
            self.key = j
        for i in text:
            if i in self.alphabet_lower:
                cipher += chr(((ord(i) - self.ord_first_letter_lower - self.key) % 32) + self.ord_first_letter_lower)
            elif i in self.alphabet_upper:
                cipher += chr(((ord(i) - self.ord_first_letter_upper - self.key) % 32) + self.ord_first_letter_upper)
            else:
                cipher += i

        return cipher

class Ven:
    def __init__(self, key):
        self.key = key
        # self.ord_first_letter_lower = ord('а')
        # self.ord_first_letter_upper = ord('А')
        # self.alphabet_lower = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
        # self.alphabet_upper = self.alphabet_lower.upper()

    def encrypt(self, text):
        self.key = self.key * (len(text) // len(self.key)) + self.key[:len(text) % len(self.key)]
        cipher = ''.join(map(chr, [i ^ x for i, x in zip(map(ord, text), map(ord, self.key))]))

        return cipher

    def decrypt(self, text):
        return self.encrypt(text)





def caesar_cipher(text):
    print('Шифр Цезаря')
    key = 3
    # key = random.randint(1, 100)
    caesar = Caesar(key)
    encrypted = caesar.encrypt(text)

    print("Ключ: ", key)
    print("Зашифрованный ключ: ", encrypted)
    print("Расшифрованный ключ:", caesar.decrypt(encrypted))
    print('-----------------------------------------')
    print("Без ключа: ", caesar.decrypt_within(encrypted))
def ven_cipher(text):
    print('Шифр В')
    # key = 'мир'
    key = input('Введите ключ: ')
    # letters = 'абвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key = ''.join([random.choice(letters)
        for _ in range(random.randint(1, 10))])
    ven = Ven(key)
    encrypted = ven.encrypt(text)
    print("Ключ: ", key)
    print("Зашифрованный ключ: ", encrypted)
    print("Расшифрованный ключ:", ven.decrypt(encrypted))

def main():
    # main_text = input('Введите текст, который хотите зашифровать: ')
    main_text = 'А ещё стремящиеся вытеснить традиционное производство,' \
                ' нанотехнологии призваны к ответу.' \
                ' Господа, внедрение современных методик' \
                ' в значительной степени обусловливает важность модели развития.' \
                ' Задача организации, в особенности же семантический разбор внешних' \
                ' противодействий представляет собой интересный' \
                ' эксперимент проверки прогресса профессионального сообщества.'
    caesar_cipher(main_text)
    ven_cipher(main_text)

if __name__ == '__main__':
    main()