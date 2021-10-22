from collections import Counter

max_ord = 65536

def encrypt(k, m):
    # Зашифровка сообщения 
    return ''.join(map(chr, [(x + k) % max_ord for x in map(ord, m)]))

def decrypt(k, m):
    # Расщифровка сообщения
    return ''.join(map(chr, [(x - k) % max_ord for x in map(ord, m)]))

def hacking(m):
    '''
    Метод Counter.most_common() возвращает список наиболее распространенных элементов 
     '''
    most_common = Counter(m).most_common()[0][0]
    # Вычисляем ключ, зная, что наиболее встречающийся символ в шифре -пробел
    key = ord(most_common) - ord(' ')
    return decrypt(key, m)

def encrypt_vern(k, m):
    k = k * (len(m) // len(k)) + k[:len(m) % len(k)]
    return ''.join(map(chr, [(x ^ y)%max_ord for x, y in zip(map(ord, m), map(ord, k))]))

def decrypt_vern(k, m):
    return encrypt_vern(k, m)

key = int(input('Введите ключ для шифра Цезаря: '))
text ='Вот, например, не трусил же теперешний прокуратор Иудеи, а бывший трибун в легионе, тогда, в Долине Дев, когда яростные германцы чуть не загрызли Крысобоя-Великана. Но, помилуйте меня, философ! Неужели вы, при вашем уме, допускаете мысль, что из-за человека, совершившего преступление против кесаря, погубит свою карьеру прокуратор Иудеи?'
print('Текст без ключа:',text)
print()
text1 = encrypt(key, text)
print('Зашифрованный текст шифра Цезаря:', text1)
print()
print('Расшифрованный текст шифра Цезаря:', decrypt(key, text1))
print()
print('Взломанный текст шифра Цезаря:', hacking(text1))
print()
key = input('Введите ключ для шифра Вернама: ')
print('Текст без ключа:',text)
print()
text1 = encrypt_vern(key, text)
print('Зашифрованный текст шифра Вернама:', text1)
print()
print('Расшифрованный текст шифра Вернама:', decrypt_vern(key, text1))