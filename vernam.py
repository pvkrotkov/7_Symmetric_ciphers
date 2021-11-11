import random
from operator import xor

msg = '''Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s.'''
key = []
while len(key) != len(msg):
    key.append(random.randint(1,10))


def encrypt(text, key):
    ecrmsg = ''
    for i, k in zip(text, key):
        ecrmsg += chr(ord(i) + k)
    print(ecrmsg)
    return ecrmsg

emsg = encrypt(msg, key)


def decrp(text, key):
    decrmsg = ''
    for i, k in zip(text, key):
      decrmsg += chr(ord(i) - k)
    print(decrmsg)
    return decrmsg

decrp(emsg, key)

