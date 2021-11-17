from collections import Counter
import random

# зашифровка методом цезаря
def encrypt(k, m):
    set_ords = [(x + k) % 65536 for x in map(ord, m)]
    return ''.join(map(chr, set_ords))

# расшифровка методом Цезаря
def decrypt(k, m):
    set_ords = [(x - k) % 65536 for x in map(ord, m)]
    return ''.join(map(chr, set_ords))

# поиск чаще всего встречающегося элемента и дешифровка без знания ключа методом Цезаря
def hack(m):
    most_common = Counter(m).most_common()[0][0]
    key = ord(most_common) - ord(' ')
    return decrypt(key, m)


# зашифровка методом Вижинера
def create_keyvi(leng):
    keyvi = []
    for i in range(leng):
        keyvi.append(random.randint(0, 255))
    return keyvi


def encryptvi(text, keyvi):
    text = list(text)
    for i in range(len(text)):
        text[i] = chr(ord(text[i]) ^ keyvi[i])
    return text

# дешифровка
def decryptvi(text, keyvi):
    return "".join(encryptvi(text, keyvi))


# text = input("Введите любой текст: ")

text = "Классический шифр Цезаря предполагает смещение каждой буквы "

# метод Цезаря
key = int(input('Введите ключ: '))
textsh = encrypt(key, text)
print("Исходный текст: ", text)
print('Зашифрованный текст методом Цезаря: ', textsh)
print('Расшифрованный текст методом Цезаря:  ', decrypt(key, textsh))
print('Взломанный текст методом Цезаря: ', hack(textsh))


#метод Вижинера
keyvi = create_keyvi(len(list(text)))
x = encryptvi(text, keyvi)
y = decryptvi(x, keyvi)
print("Зашифрованный текст методом Вижинера: ", "".join(x))
print("Расшифрованный  текст методом Вижинера: ", y)







