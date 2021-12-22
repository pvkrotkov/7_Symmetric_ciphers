def decrypt(word):
    keys = {}
    for letter in word:
        keys[letter] = keys.get(letter, 0) + 1
    key = sorted(keys.items(), key=lambda x: x[1], reverse=True)[0]
    return chr(ord(key[0]) - ord(" "))
def encryption(word, key, decode=False):
    ls = []
    for i in word:
        if decode:
            ls.append(chr((ord(i) - ord(key)) % 65536))
        else:
            ls.append(chr(ord(i) + ord(key) % 65536))
    return "".join(ls)

def decode_encode(text, key): #XOR
    ls = []
    for a in range(len(text)):
        for i, j in [(text[a], key[a])]:
            ls.append(ord(i) ^ ord(j))
    return "".join(map(chr, ls))
text = "Hello world"
key = "jgqwertagsh"
enc = decode_encode(text, key)

print(f'Запуск...')
dec = decode_encode(enc, key)

print()
print(f'Шифрование...')
print()
if __name__ == '__main__':

    text = "My name is Maya"
    key = "I"

    encrypted_text = encryption(text, key)
    decrypted_text = encryption(encrypted_text, key, decode=True)

    print(f"{text} -> «{encrypted_text}» -> {decrypted_text}")

    print(f"Подобранный ключ: {decrypt(encrypted_text)}")
    print()
