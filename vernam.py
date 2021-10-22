import random


def create_key(leng):
    key = []
    for i in range(leng):
        key.append(random.randint(0,255))
    return key


def encrypt(text, key):
    text = list(text)
    for i in range(len(text)):
        text[i] = chr(ord(text[i]) ^ key[i])
    return text


def decrypt(text, key):
    return "".join(encrypt(text, key))


text = input()
key = create_key(len(list(text)))
print(list(text))
a = encrypt(text, key)
b = decrypt(a, key)
print(b)

