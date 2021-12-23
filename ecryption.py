from collections import Counter


def caesar_encrypt(k, m):
    k %= 65536
    res = [chr((ord(char) + k) % 65536 + 65536 * (ord(char) + k < 0)) for char in m]
    return ''.join(res)


def caesar_decrypt(k, c):
    k %= 65536
    res = [chr((ord(char) - k) % 65536 + 65536 * (ord(char) < k)) for char in c]
    return ''.join(res)


def caesar_decrypt_without_key(c):
    by_frequency = sorted(Counter(c))
    print('Identified key:', ord(by_frequency[0]) - ord(' '))
    return caesar_decrypt(ord(by_frequency[0]) - ord(' '), c)


def vernam_encrypt(k, m):
    k *= len(m) // len(k)
    k += k[:len(m) % len(k)]
    return ''.join(map(chr, [char ^ key for char, key in zip(map(ord, m), map(ord, k))]))


def vernam_decrypt(k, c):
    return vernam_encrypt(k, c)


cipher_name = int(input('Please, enter 1 for choosing Caesar cipher, or 2 for choosing Vernam cipher: '))
command = int(input('\nEnter 1 if you want to encrypt a text, or 2 if you want to decrypt a text: '))
if cipher_name == 1:
    if command == 1:
        k = int(input('\nEnter the cipher key: '))
        m = input('Enter the text to encrypt: ')
        print('Result:', caesar_encrypt(k, m))
    elif command == 2:
        c = input('\nEnter the text to decrypt: ')
        is_key_known = input('Enter 1 if you know the cipher key, or else enter 2: ') == '1'
        if is_key_known:
            k = int(input('Enter the cipher key: '))
            print('Result:', caesar_decrypt(k, c))
        else:
            print('The decrypted text probably is:', caesar_decrypt_without_key(c))
elif cipher_name == 2:
    if command == 1:
        k = input('\nEnter the keys separated by a space: ')
        m = input('Enter the text to encrypt: ')
        print('Result: ', vernam_encrypt(k, m))
    elif command == 2:
        k = input('\nEnter the keys separated by a space: ')
        c = input('Enter the text to decrypt: ')
        print('Result: ', vernam_decrypt(k, c))
