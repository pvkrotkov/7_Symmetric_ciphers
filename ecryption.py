

max_ord = 65536


def encrypt(k, m):
    return ''.join(map(chr, [(x + k) % max_ord for x in map(ord, m)]))


def decrypt(k, c):
    return ''.join(map(chr, [(x - k) % max_ord for x in map(ord, c)]))


def decrypt_(c):
    symbols = set(c)
    l = [0, '']
    from re import findall
    for i in symbols:
        l = (len(findall(r'{}'.format(i), c)), i) if len(
            findall(r'{}'.format(i), c)) > l[0] else l
    k = ord(l[1]) - ord(' ')
    return ''.join(map(chr, [(x - k) % max_ord for x in map(ord, c)]))


def vernam(k, m):
    k = k*(len(m)//len(k)) + k[-(len(m) % len(k)):]
    return ''.join(map(chr, [i ^ x for i, x in zip(map(ord, m), map(ord, k))]))


def vernam_decrypt(k, c):
    return vernam(k, c)


k = 1000
text = 'Место тяги было продившим от снега. Сам он вернулся на другой край, к двойняшке-березе, и, прислонив ружье к развилине сухого нижнего сучка, снял кафтан, перепоясался и попробовал свободы движений рук.Старая седая Ласка, ходившая за ним следом, села осторожно против него и насторожила уши. Солнце спускалось за крупный лес, и на свете зари березки, рассыпанные по осиннику, отчетливо рисовались своими висящими ветвями с надутыми, готовыми лопнуть почками.'
a = encrypt(k, text)
print()
print('Текст, зашифрованный шифром Цезаря: ', a, '\n')
b = decrypt(k, a)
print('Текст, расшифрованный с ключом: ', b, '\n')
c = decrypt_(a)
print('Без ключа: ', c, '\n')
k = input('ключ для Вернама: ')
print()
d = vernam(k, text)
print('Шифротекст Вернама: ', d, '\n')
print('Расшифрованный текст: ', vernam_decrypt(k, d))
