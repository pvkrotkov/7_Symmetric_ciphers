from collections import Counter


MAX_ORD = 65536


def encrypt(k, m):
    offset_ords = [(x + k)%MAX_ORD for x in map(ord, m)]
    return ''.join(map(chr, offset_ords))


def decrypt(k, m):
    offset_ords = [(x - k)%MAX_ORD for x in map(ord, m)]
    return ''.join(map(chr, offset_ords))


def hack(m):
    most_common = Counter(m).most_common()[0][0]
    key = ord(most_common) - ord(' ')
    return decrypt(key, m)


key = int(input('Введите ключ: '))
d = encrypt(key, 'Классический шифр Цезаря предполагает смещение каждой буквы текста на следующую за ней через три. Последние буквы смещаются в начало алфавита по кольцу. Мы будем использовать модифицированный алгоритм, в котором ключом является целое число - величина смещения.')
print('Зашифрованный текст:', d)
print()
print('Расшифрованный текст:', decrypt(key, d))
print()
print('Взломанный текст:', hack(d))