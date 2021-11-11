import random

k = random.randint(1,10) or random.randint(10**3, 10**4)
msg = '''Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s.'''

def encryption(text):
    btext = [ord(i)+k for i in text]
    ecrText = ''
    for i in btext:
        ecrText += chr(i)
    print('Encryption message: ',ecrText)
    return btext
btext = encryption(msg)

print('')

def decryption(bytes):
    text = ''
    for i in range(len(bytes)):
        text += chr(bytes[i] - k)
    print('Decryption message: ',text)
    return text

decryption(btext)

print('')

def breaking(bytes):
    count = sorted([(bytes.count(i), i) for i in set(bytes)], reverse=True)
    space = count[0]

    key = int(count[0][1]) - ord(' ')
    text = ''
    for i in bytes:
        text += chr(i - key)
    print('Hacked encryption: ',text)
    return text

breaking(btext)