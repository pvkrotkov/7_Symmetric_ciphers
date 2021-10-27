def encrypt(key, text):
    result = ""
    key = [ord(symbol) for symbol in key]
    for i in range(len(text)):
        code = ord(text[i])
        code += key[i % len(key)]
        result += chr(code % 65536)
    return result


def decrypt(key, text):
    result = ""
    key = [ord(symbol) for symbol in key]
    for i in range(len(text)):
        code = ord(text[i])
        code -= key[i % len(key)]
        result += chr(code % 65536)
    return result


inp = input("Enter a string: ")
k = input("Enter a key: ")
enc = encrypt(k, inp)
print(f"String: {inp}\nEncrypted: {enc}\nDecrypted: {decrypt(k, enc)}")