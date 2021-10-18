from collections import Counter


MAX_ORD = 65536


def encrypt_caesar(k, m):
    offset_ords = [(x + k)%MAX_ORD for x in map(ord, m)]
    return ''.join(map(chr, offset_ords))


def decrypt_caesar(k, m):
    offset_ords = [(x - k)%MAX_ORD for x in map(ord, m)]
    return ''.join(map(chr, offset_ords))


def hack_caesar(m):
    most_common = Counter(m).most_common()[0][0]
    key = ord(most_common) - ord(' ')
    return decrypt_caesar(key, m)


def encrypt_vernam(k, m):
    k = k * (len(m) // len(k)) + k[:len(m) % len(k)]
    offset_ords = [(x ^ y)%MAX_ORD for x, y in zip(map(ord, m), map(ord, k))]
    return ''.join(map(chr, offset_ords))


def decrypt_vernam(k, m):
    return encrypt_vernam(k, m)


key = int(input('Введите ключ для Цезаря: '))
text = encrypt_caesar(key, 'Классический шифр Цезаря предполагает смещение каждой буквы текста на следующую за ней через три. Последние буквы смещаются в начало алфавита по кольцу. Мы будем использовать модифицированный алгоритм, в котором ключом является целое число - величина смещения.')
print('Зашифрованный текст Цезаря:', text)
print()
print('Расшифрованный текст Цезаря:', decrypt_caesar(key, text))
print()
print('Взломанный текст Цезаря:', hack_caesar(text))
print()
key = input('Введите ключ для Вернама: ')
text = input('Введите текст для Вернама: ')
text = encrypt_vernam(key, text)
print('Зашифрованный текст Вернама:', text)
print()
print('Расшифрованный текст Вернама:', decrypt_vernam(key, text))
