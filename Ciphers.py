import collections, re


# print(ord(" "))
# print(chr(ord(" ")))
txt = 'Некоторый текст для ареолы с о с мыслом которой нельзя не согласиться'

key = 'lambda'
def cesar_encrypt(k, string):
    new_str = ''
    for elem in string:
        elem = chr((ord(elem)+k)%65536)
        new_str += elem
    print(new_str)
    return new_str


def cesar_decrypt(string):
    new_str = ''
    punct = ',.!?:;'
    count = collections.Counter()
    new_str = ''
    ltxt = [w.rstrip(punct).lower() for w in string if len(w.rstrip(punct)) == 1]

    k = ord(str(*sorted(set(ltxt), key=ltxt.count, reverse=True)[:1])) - (ord(" "))

    for elem in string:
        elem = chr((ord(elem)-k)%65536)
        new_str += elem

    print(new_str)
    return new_str


# cesar_decrypt(cesar_encrypt(-5, txt))  # Example


def vijen_encrypt(k, string):
    if len(k) > len(string):
        k = k[:len(string)]
        for i in range(len(string)-len(k)):
            k += k[i]
    else:
        k = k*((len(string)-len(k))//len(k))
        for i in range(len(string)-len(k)):
            k += k[i]
    new_str = ''

    for i in range(len(k)):
        new_str += chr((ord(string[i])+ord(k[i])%65536))

    return new_str



def vijen_decrypt(k, string):
    if len(k) > len(string):
        k = k[:len(string)]
        for i in range(len(string)-len(k)):
            k += k[i]
    else:
        k = k*((len(string)-len(k))//len(k))
        for i in range(len(string)-len(k)):
            k += k[i]
    new_str = ''
    for i in range(len(k)):
        new_str += chr((ord(string[i])-ord(k[i])%65536))

    return new_str

# Examples
# print(vijen_encrypt(key, txt))
# print(vijen_decrypt(key, vijen_encrypt(key, txt)))


def vernam_OTP(k, string):
    if len(k) > len(string):
        k = k[:len(string)]
        for i in range(len(string)-len(k)):
            k += k[i]
    else:
        k = k*((len(string)-len(k))//len(k))
        for i in range(len(string)-len(k)):
            k += k[i]


    xored = [sym ^ ord(k[i]) for i, sym in enumerate([x for x in map(ord, string)])]
    new_str = ''.join(map(chr, xored))
    return new_str


# Examples
random_key = 'lambda'
# print(vernam_OTP(random_key, txt))
# print(vernam_OTP(random_key, vernam_OTP(random_key, txt)))