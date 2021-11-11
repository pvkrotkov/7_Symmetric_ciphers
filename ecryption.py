import string,binascii
from random import randint
from re import findall

def caes_encrypt(k, m):
    return ''.join(map(chr, [x + k for x in map(ord, m)]))

def caes_decrypt(k,m):
    return ''.join(map(chr, [x - k for x in map(ord, m)]))
#---------
def vi_encrypt(k,m):
    text = str()
    alph = string.ascii_lowercase
    for ind, let in enumerate(m):
        if let in alph:
            letter_ind = alph.index(let)
        key = alph.index(k[ind%len(k)])
        letter_ind = (letter_ind + key)%26
        text += alph[letter_ind]
    return text

def vi_decrypt(k,m):
    text = str()
    alph = string.ascii_lowercase
    for ind, let in enumerate(m):
        if let in alph:
            letter_ind = alph.index(let)
        key = alph.index(k[ind%len(k)])
        letter_ind = (letter_ind - key)%26
        text += alph[letter_ind]
    return text
#----------    
def ver_encrypt(m, k=""):
    final=""
    keys=""
    for symbol in m:
        key = randint(0,32); keys += str(key) + "/"
        final += chr((ord(symbol) + key - 17)%33 + ord('A'))
    print('Зашифрованное сообщение: ', final)
    print ('Ключ шифрования: ',keys)

def ver_decrypt(m, k): 
    keys =  k.split('/')
    final = ''
    for i, symbol in enumerate(m):
        if keys[i] != '':
            final += chr((ord(symbol) - int(keys[i])- 17)%33 + ord('A'))
    print ('Расшифрованное сообщение : ', final)


#print(caes_encrypt(2, 'Hello!'))
#print(caes_decrypt(2, 'Jgnnq#'))

#print(vi_encrypt('world','message'))
#print(vi_decrypt('world','isjddcs'))

#ver_encrypt('DAHHK')
#ver_decrypt('WUQPU', '1/2/24/23/25/')