import random
import string

import ciphering


def _main():
    text = 'Прекрасная и чудесная пора – осень, она дарит последние ' \
           'теплые дни в году, окрашивает все вокруг в удивительные  ' \
           'и сказочные цвета, и я очень люблю осень, ведь она всегда ' \
           'дарит новые впечатления и приключения. '        
    caesar_test(text)
    vigenere_test(text)


def caesar_test(text):
    print('_____ Тестирование Шифра Цезаря _____')
    key = random.randint(1, 100)
    caesar = ciphering.Caesar(key)
    encrypted = caesar.encrypt(text)
    print('Ключ:', key)
    print('Шифр:', encrypted)
    print('Расшифровка:', caesar.decrypt(encrypted))
    print('Взлом:', ciphering.Caesar.hack(encrypted))


def vigenere_test(text):
    print('____ Тестирование Шифра Вижинера _____')
    key = ''.join([
        random.choice(string.ascii_letters)
        for _ in range(random.randint(1, 10))
    ])
    vigenere = ciphering.Vigenere(key)
    encrypted = vigenere.encrypt(text)
    print('Ключ:', key)
    print('Шифр:', encrypted)
    print('Расшифровка:', vigenere.decrypt(encrypted))


if __name__ == '__main__':
    _main()
