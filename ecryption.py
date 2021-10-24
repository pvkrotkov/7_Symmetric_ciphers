from collections import Counter
N = 65536

def encrypt_caesar(k, m): #зашифровка сообщения
    offset_ords = [(x + k)%N for x in map(ord, m)]
    return ''.join(map(chr, offset_ords))


def decrypt_caesar(k, m): #расшифровка сообщения
    offset_ords = [(x - k)%N for x in map(ord, m)]
    return ''.join(map(chr, offset_ords))


def hack(m):
    most_common = Counter(m).most_common()[0][0]
    key = ord(most_common) - ord(' ')
    return decrypt_caesar(key, m)


def encrypt_vernam(k, m):
    k = k * (len(m) // len(k)) + k[:len(m) % len(k)]
    offset_ords = [(x ^ y)%N for x, y in zip(map(ord, m), map(ord, k))]
    return ''.join(map(chr, offset_ords))


def decrypt_vernam(k, m):
    return encrypt_vernam(k, m)




key = int(input('Введите ключ для Цезаря: '))
text = encrypt_caesar(key, '''Мне нравится, что вы больны не мной,
Мне нравится, что я больна не вами,
Что никогда тяжелый шар земной
Не уплывет под нашими ногами''')
print('Зашифрованный текст Цезаря:', text)
print('Расшифрованный текст Цезаря:', decrypt_caesar(key, text))
print('Взломанный текст Цезаря:', hack(text))
print('----------------------------------------------------------------------------------')
key = input('Введите ключ для Вернама: ')
text = input('Введите текст для Вернама: ')
text = encrypt_vernam(key, text)
print('Зашифрованный текст Вернама:', text)
print('Расшифрованный текст Вернама:', decrypt_vernam(key, text))
