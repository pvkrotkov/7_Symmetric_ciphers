

max_k = 100


def encrypt(k, m):
    return ''.join(map(chr, [x + k for x in map(ord, m)]))


def decrypt(k, c):
    return ''.join(map(chr, [x-k for x in map(ord, c)]))


def decrypt_(c):
    symbols = set(c)
    l = [0, '']
    from re import findall
    for i in symbols:
        l = (len(findall(r'{}'.format(i), c)), i) if len(
            findall(r'{}'.format(i), c)) > l[0] else l
    k = ord(l[1]) - ord(' ')
    return ''.join(map(chr, [x-k for x in map(ord, c)]))


def random_int(l, maximum):
    from random import randint
    return [randint(1, maximum) for i in range(l)]


def vernam(m):
    a = random_int(len(m), max_k)
    return ''.join(map(chr, [x + a[i] for i, x in enumerate(map(ord, m))])), a


def vernam_decrypt(k, c):
    return ''.join(map(chr, [x - k[i] for i, x in enumerate(map(ord, c))]))


k = 1000
text = 'Место тяги было продившим от снега. Сам он вернулся на другой край, к двойняшке-березе, и, прислонив ружье к развилине сухого нижнего сучка, снял кафтан, перепоясался и попробовал свободы движений рук.Старая седая Ласка, ходившая за ним следом, села осторожно против него и насторожила уши. Солнце спускалось за крупный лес, и на свете зари березки, рассыпанные по осиннику, отчетливо рисовались своими висящими ветвями с надутыми, готовыми лопнуть почками.'
a = encrypt(k, text)
# print(a)
b = decrypt(k, a)
# print(b)
c = decrypt_(a)
# print(c)
d, key = vernam(text)
# print(d)
#print(vernam_decrypt(key, d))
