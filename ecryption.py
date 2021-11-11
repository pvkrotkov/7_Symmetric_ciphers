from collections import Counter
MAX_ORD = 65536


def encrypt_caesar(key, m):
    offset_ords = [(x + key)%MAX_ORD for x in map(ord, m)]
    return ''.join(map(chr, offset_ords))


def decrypt_caesar(key, m):
    offset_ords = [(x - key)%MAX_ORD for x in map(ord, m)]
    return ''.join(map(chr, offset_ords))




def encrypt_vernam(key, m):
    key = key * (len(m) // len(key)) + key[:len(m) % len(key)]
    offset_ords = [(x ^ y)%MAX_ORD for x, y in zip(map(ord, m), map(ord, key))]
    return ''.join(map(chr, offset_ords))


def decrypt_vernam(key, m):
    return encrypt_vernam(key, m)


key = int(input('Введите ключ для Цезаря: '))
text = encrypt_caesar(key, 'Мальчик-хулиган пять дней не мог попасть домой. Он звонил в дверь и убегал.')
print('Зашифрованный текст Цезаря:', text)
print()
print('Расшифрованный текст Цезаря:', decrypt_caesar(key, text))
print()
key = input('Введите ключ для Вернама: ')
text = input('Введите текст для Вернама: ')
text = encrypt_vernam(key, text)
print('Зашифрованный текст Вернама:', text)
print()
print('Расшифрованный текст Вернама:', decrypt_vernam(key, text))
