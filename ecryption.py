big_en = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
          'U', 'V', 'W', 'X', 'Y', 'Z']
small_en = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']

small_ru = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у',
            'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

big_ru = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф',
          'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']

symbols = [';', ',', '.', ' ', ':', '!', '?', '^', '+', '-', '_']


def ceasar_crypt(text, n):
    crypted_text = []
    for i in text:
        alphabet = 1
        if i in big_en:
            alphabet = big_en
        elif i in small_en:
            alphabet = small_en
        elif i in small_ru:
            alphabet = small_ru
        elif i in big_ru:
            alphabet = big_ru
        elif i in symbols:
            crypted_text.append(i)
            alphabet = -1

        if alphabet != 1 and alphabet != -1:
            index = alphabet.index(i)
            changing = (index + n) % 26
            new_elem = alphabet[changing]
            crypted_text.append(new_elem)
        elif alphabet != -1:
            print(f'Данный элемент не существует в словаре - {i}')
    return crypted_text


def cipher_decrypt_lower(text_to, key):
    decrypted = ""
    for i in text_to:
        alphabet = 1
        if i in big_en:
            alphabet = big_en
        elif i in small_en:
            alphabet = small_en
        elif i in small_ru:
            alphabet = small_ru
        elif i in big_ru:
            alphabet = big_ru
        elif i in symbols:
            decrypted += i

        if alphabet != 1:
            c_index = alphabet.index(i)

            c_og_pos = (c_index - key) % 26

            c_og = alphabet[c_og_pos]

            decrypted += c_og
    return decrypted


def encrypt_vernam(plaintext, key):
    k = len(key)
    keys_indexes = [ord(i) for i in key]
    letters_indexes = [ord(i) for i in plaintext]
    crypted_text = ''
    for i in range(len(letters_indexes)):
        elem = (letters_indexes[i] + keys_indexes[i % k]) % 26
        crypted_text += chr(elem + 65)
    return crypted_text


def decrypt_vernam(crypted_text, key):
    k = len(key)
    keys_indexes = [ord(i) for i in key]
    crypted_text_int = [ord(i) for i in crypted_text]
    plaintext = ''
    for i in range(len(crypted_text_int)):
        elem = (crypted_text_int[i] - keys_indexes[i % k]) % 26
        plaintext += chr(elem + 65)
    return plaintext


print('ШИФР ЦЕЗАРЯ')
code = ''.join(ceasar_crypt('Mir привет!', 2))
print(code)

for j in range(1, 34):
    decrypted = cipher_decrypt_lower(code, j)
    print(f'Для шага {j}: {decrypted}')
print()
print('ШИФР ВЕРНАМА')
text_to_vernam = 'helloworld'
key_vernam = 'ea'
vernam = encrypt_vernam(text_to_vernam.upper(), key_vernam.upper())
print('Зашифрованный текст: ', vernam)
re_vernam = decrypt_vernam(vernam, key_vernam.upper())
print('Изначальный текст: ', re_vernam)
