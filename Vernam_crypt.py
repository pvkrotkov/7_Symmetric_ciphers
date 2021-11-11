import random


def create_key(leng):  # генерация ключа
    key = []
    for i in range(leng):
        key.append(random.randint(0, 255))
    return key


def encrypt(text, key):  # шифрование текста
    text = list(text)
    for i in range(len(text)):
        text[i] = chr(ord(text[i]) ^ key[i])
    return text


def decrypt(text, key):  # расшифровка текста
    return "".join(encrypt(text, key))


# text = input("Введите текст: ")
text = "Смогу ли я переступить или не смогу! Осмелюсь ли нагнуться и взять или нет? Тварь ли я дрожащая или право имею… "
print("Исходный текст: ", text)
key = create_key(len(list(text)))  # создание ключа
a = encrypt(text, key)  # шифровка
b = decrypt(a, key)  # расшифровка
print("Зашифрованный текст: ")
print("".join(a))
print("Расшифрованный  текст: ")
print(b)
