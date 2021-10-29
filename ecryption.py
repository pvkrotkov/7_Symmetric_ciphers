from collections import Counter
from random import randint

TEST_TEXT = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently  with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

# шифрование цезарем
def encrypt_caesar(k, m):
    return ''.join(map(chr, [abs(x + k) for x in map(ord, m)]))

# дешифрование цезарем
def decrypt_caesar(k, m):
    return ''.join(map(chr, [abs(x - k) for x in map(ord, m)]))

# взлом шифра на основе факта, что пробел - самый частовстречающийся символ текста
def hack_caesar(cryptotext):
    true_space = ord(' ')
    fake_space = ord(Counter(cryptotext).most_common()[0][0])
    key = abs(true_space - fake_space)

    return decrypt_caesar(key, cryptotext)


# шифр вернама - шифр вижинера с неограниченным неповторяющимся ключом
def generate_key(length):
    return [randint(0,26) for _ in range(length)]

def xor(char, key):
    return chr(ord(char)^key)

def encrypt_otp(text):
    key = generate_key(len(text))
    return ''.join([xor(text[i], key[i]) for i in range(len(text))]), key

def decrypt_otp(cryptotext, key):
    return ''.join([xor(cryptotext[i], key[i]) for i in range(len(cryptotext))])



print(encrypt_caesar(2, 'Hello!'))
print(decrypt_caesar(2, 'Jgnnq#'))

cryptotext = encrypt_caesar(4, TEST_TEXT)
print(f'\nЗашифрованный шифром Цезаря текст: {cryptotext}')
print(f'\nВзлом шифра Цезаря: {hack_caesar(cryptotext)}')

encryptedtext, key = encrypt_otp(TEST_TEXT)
print(f'\n\nЗашифрованный шифром Вернама текст: {encryptedtext}')
decryptedtext = decrypt_otp(encryptedtext, key)
print(f'\nРасшифрованный текст: {decryptedtext}')
