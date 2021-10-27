from collections import Counter
# Task 1


def encrypt(key, text):
    result = ""
    for symbol in text:
        code = ord(symbol)
        code += key
        result += chr(code % 65536)
    return result


def decrypt(key, text):
    result = ""
    for symbol in text:
        code = ord(symbol)
        code -= key
        result += chr(code % 65536)
    return result


# Task 2


def decrypt_no_key(text):
    """
    Предполагаем, что чаще всего встречается пробел. С помощью объекта Counter из модуля collections получим
    отсортированный по значениям словарь вхождений элементов в строку (словар имеет вид 'символ': количество вхождений)
    Ключ получим в виде разницы позиции в Unicode таблице наиболее часто встречающегося символа и пробела
    Далее вызовем функцию расшифровки, которую реализовали в первом задании.
    В качестве ключа передадим вычисленное значение.
    """
    symbol = Counter(text).most_common(1)[0][0]
    key = ord(symbol) - ord(" ")
    return encrypt(key, text)


inp = input("Enter a string: ")
k = int(input("Enter a key: "))
enc = encrypt(k, inp)
print(f"String: {inp}\nEncrypted: {enc}\nDecrypted: {decrypt(k, enc)}\nDecrypted without key: {decrypt_no_key(inp)}")


