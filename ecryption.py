def encrypt(k, m):
    return ''.join(map(chr, [x + k for x in map(ord, m)]))
from collections import Counter
N = 65536

print(encrypt(2, 'Hello!')) 

def encrypt_caesar(k, m):
    offset_ords = [(x + k)%N for x in map(ord, m)]
    return ''.join(map(chr, offset_ords))


def decrypt_caesar(k, m):
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
text = encrypt_caesar(key, 'Фатальный недостаток шифра Цезаря, как мы говорили то, что каждый символ текста преобразуется в один и тот же символ шифротекста. Это можно исправить используя ключ длиной не в одно число, а в несколько. Тогда первый символ смещается на первое число в ключе, второй  на второе и так далее.')
print('Зашифрованный текст Цезаря:', text)
print('---------------------------------------------------------------------------')
print('Расшифрованный текст Цезаря:', decrypt_caesar(key, text))
print('-----------------------------------------------------------------------------')
print('Взломанный текст Цезаря:', hack(text))
print('------------------------------------------------------------------------------')
key = input('Введите ключ для Вернама: ')
print('------------------------------------------------------------------------------')
text = input('Введите текст для Вернама: ')
print('----------------------------------------------------------------------------------')
text = encrypt_vernam(key, text)
print('Зашифрованный текст Вернама:', text)
print('--------------------------------------------------------------------------------')
print('Расшифрованный текст Вернама:', decrypt_vernam(key, text))
