import random


def create_key(leng): #генерируем ключ
    key = []
    for i in range(leng):
        key.append(random.randint(0,255))
    return key


def encrypt(text, key): # шифруем текст
    text = list(text)
    for i in range(len(text)):
        text[i] = chr(ord(text[i]) ^ key[i])
    return text


def decrypt(text, key): #расшифровываем текст
    return "".join(encrypt(text, key))


text = input("Введите текст")
key = create_key(len(list(text))) # создаем ключ
a = encrypt(text, key) # шифрование
b = decrypt(a, key) #расшифрование
print("Закодированый текст")
print("".join(a))
print("Раскодированый закодированый текст")
print(b)

