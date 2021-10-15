import random
import string

import cipher


def _main():
    text = 'Так говорила в июле 1805 года известная Анна Павловна Шерер, ' \
           'фрейлина и приближенная императрицы Марии Феодоровны, встречая ' \
           'важного и чиновного князя Василия, первого приехавшего на ее ' \
           'вечер. '
    caesar_test(text)
    vigenere_test(text)


def caesar_test(text):
    print('--- Тестирование Шифра Цезаря ---')
    key = random.randint(1, 100)
    caesar = cipher.Caesar(key)
    encrypted = caesar.encrypt(text)
    print('Ключ:', key)
    print('Шифр:', encrypted)
    print('Расшифровка:', caesar.decrypt(encrypted))
    print('Взлом:', cipher.Caesar.hack(encrypted))


def vigenere_test(text):
    print('--- Тестирование Шифра Вижинера ---')
    key = ''.join([
        random.choice(string.ascii_letters)
        for _ in range(random.randint(1, 10))
    ])
    vigenere = cipher.Vigenere(key)
    encrypted = vigenere.encrypt(text)
    print('Ключ:', key)
    print('Шифр:', encrypted)
    print('Расшифровка:', vigenere.decrypt(encrypted))


if __name__ == '__main__':
    _main()
