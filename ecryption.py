from collections import Counter

maxOrd = 65536

def encrypt_caesar(k, m):
    offset_ords = [(x + k) % maxOrd for x in map(ord, m)]
    return ''.join(map(chr, offset_ords))


def decrypt_caesar(k, m):
    offset_ords = [(x - k) % maxOrd for x in map(ord, m)]
    return ''.join(map(chr, offset_ords))


def hack_caesar(m):
    most_common = Counter(m).most_common()[0][0]
    key = ord(most_common) - ord(' ')
    return decrypt_caesar(key, m)


def encrypt_vernam(k, m):
    k = k * (len(m) // len(k)) + k[:len(m) % len(k)]
    offset_ords = [(x ^ y) % maxOrd for x, y in zip(map(ord, m), map(ord, k))]
    return ''.join(map(chr, offset_ords))


def decrypt_vernam(k, m):
    return encrypt_vernam(k, m)


key = int(input('Введите ключ для шифра Цезаря: '))
text = encrypt_caesar(key, 'Скажите, когда возникло пространство и его мимолетная невеста — время, когда родилось их дитя — материя, вместе с которыми наступили и страдания мира? Ибо вместе с пространством началось страдание, вместе с временем — смерть')
print('Зашифрованный текст Цезаря:', text, '\n')
print('Расшифрованный текст Цезаря:', decrypt_caesar(key, text), '\n')
print('Взломанный текст Цезаря:', hack_caesar(text), '\n')
key = input('Введите ключ для Вернама: ')
text = input('Введите текст для Вернама: ')
text = encrypt_vernam(key, text)
print('Зашифрованный текст Вернама:', text, '\n')
print('Расшифрованный текст Вернама:', decrypt_vernam(key, text))