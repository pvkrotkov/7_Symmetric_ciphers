def encrypt(k, m): # шифрование текста
    return ''.join(map(chr, [(x + k)%65536 for x in map(ord, m)]))


def decrypt(k, m): # расшифрование текста
    return ''.join(map(chr, [(x - k)%65536 for x in map(ord, m)]))


def hack(text): # взлом текста (расшифрование без ключа) методом частотного анализа
    text1 = list(text)
    symbols = {i:text1.count(i) for i in set(text1)}
    space = max(symbols, key=symbols.get) # ищем символ соотв. пробелу
    key = ord(space)-ord(" ") # находим число-ключ
    return(decrypt(key, text))  #расшифровываем


phrase = input("Введите текст для шифрования")
seed = input("Введите число")
encoded = encrypt(seed, phrase)
print("Закодированый текст")
print(encoded)
print("Раскодированый закодированый текст")
print(decrypt(seed, encoded))
