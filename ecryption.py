from typing import Counter

def encrypt(shift, text):
    return ''.join(map(chr, [(x + shift) % 65536 for x in map(ord, text)]))

def decrypt(shift, text):
    return ''.join(map(chr, [(x - shift) % 65536 for x in map(ord, text)]))

def decrypt_without_key(text):
    occurrences = Counter(text).most_common(1)
    return (decrypt(occurrences[0][1], text))

def vernam_cipher_encrypt(key, text):
    while (len(text) > len(key)):
        key = str(input("Длина ключа должна быть больше длины сообщения, введите новый ключ: "))
    return ''.join([chr(ord(text[i]) ^ ord(key[i])) for i in range(len(text))]), key
    
def vernam_cipher_decrypt(key, text):
    return ''.join([chr(ord(text[i]) ^ ord(key[i])) for i in range(len(text))])

def main():
    # a = encrypt(3, "Hello world!z")
    # print(a)
    # print(decrypt_without_key(a))
    # print(decrypt(3, a))

    text, key = vernam_cipher_encrypt("23", "man")
    print(text)
    a = vernam_cipher_decrypt("abclo123", text)
    print(a)

if __name__ == "__main__":
    main()