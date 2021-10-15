def encrypt(k, m):
    return ''.join(map(chr, [(x + k)%65536 for x in map(ord, m)]))
def decrypt(k, m):
    return ''.join(map(chr, [(x - k)%65536 for x in map(ord, m)]))
def hack(text):
    text1 = list(text)
    symbols = {i:text1.count(i) for i in set(text1)}
    space = max(symbols, key=symbols.get)
    key = ord(space)-ord(" ")
    return(decrypt(key, text))
phrase = input()
encoded = encrypt(10, phrase)
print(hack(encoded))
