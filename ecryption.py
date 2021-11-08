from collections import Counter

N = 65536

#шифр Цезаря
def encrypt(k, m): #зашивровываем
    return ''.join(map(chr,[(x + k) % N for x in map(ord, m)]))


def decrypt(k, c): #расшифровываем
    return ''.join(map(chr, [(x - k) % N for x in map(ord, c)]))

#без знания ключа
def vz(m):
    #такой способ точно работает на длинных текстах(10 слов+), так как в них чаще встречаются пробелы
    most = Counter(m).most_common(1)[0][0]
    key = ord(most) - ord(' ')
    return decrypt(key, m)

#шифр Вернама
def encrypt_v(k, m): #зашивровываем
    k = k * (len(m) // len(k)) + k[:(len(m) % len(k))]
    k =''.join(map(chr, [i ^ x for i, x in zip(map(ord, m), map(ord, k))]))
    return k


def decrypt_v(k, c): #расшифровываем
    return encrypt_v(k, c)

def print_res():
    k = int(input('введите ключ: '))
    t="Днем в своих лабораториях они переливают лес из пробирки в пробирку, рассматривают лес под микроскопом, считают лес на арифмометрах," \
      " а лес стоит вокруг, висит над ними, прорастает сквозь их спальни, в душные предгрозовые часы приходит к их окнам толпами бродячих деревьев" \
      " и тоже, возможно, не может понять, что они такое, и зачем они вообще."
    za_t = encrypt(k, t)
    print('зашифрованный текст (Цезарь):', za_t)
    de_t = decrypt(k, za_t)
    print('расшифрованный текст (Цезарь):', de_t)
    print('расшифрованный текст (Цезарь, без знания ключа):', vz(za_t))
    k = "1 5 2 4 7 9"
    za_t_v = encrypt_v(k, t)
    de_t_v = decrypt_v(k, za_t_v)
    print('зашифрованный текст (Вернам):', za_t_v)
    print('расшифрованный текст (Вернам):', de_t_v)


if __name__ == '__main__':
     print_res()
