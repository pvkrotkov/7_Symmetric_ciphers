from random import randint
from re import findall


def Coding(k, m): #шифровка
    return ''.join([chr((ord(x) + k) % 65536) for x in m])

def Decoding(k, m): #расшифровка
    return ''.join([chr((ord(x) - k) % 65536) for x in m])

def nonkey(m): #расшифровка без ключа
    max_char = 0
    key = 0 
    for i in range(65536):
        tt = len(m.split(chr((32 + i) % 65536)))
        if tt > max_char:
            max_char = tt
            key = i            
    return key

def Regular(text):
    template = r"[0-9]+"
    return findall(template, text)

def Vernam(m, tt = '', k = ''):
    for i in m:
            key = randint(0,32); k += str(key) + "/"
            tt += chr((ord(i) + key - 17)%33 + ord('А'))
    return [tt, k]
    
def Dever(m, k, tt = ''):
        for index, i in enumerate(m):
            tt += chr((ord(i) - int(Regular(k)[index]) - 17)%33 + ord('А'))
        return tt

x = 5
a = Coding(x, 'Snap back to reality, ope there goes gravity')
print(a)
c = nonkey(a)
print(Decoding(x, a))
print(Decoding(c, a))

a = Vernam('Листья с клена падают, с ясеня. Ничего себе, ничего себе! Вот смотрю я и действительно. Хорошо, хорошо!')
print(a[0])
b = Dever(a[0], a[1])
print(b)
