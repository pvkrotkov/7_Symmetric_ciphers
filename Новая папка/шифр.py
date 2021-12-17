import random


numbers = ['%02d' % x for x in range(32)]


def caesar_encryption(phrase, step=3):
    ph = list(phrase)
    for i in range(len(ph)):
        if ph[i].islower():
            flag = True
        else:
            flag = False
        ph[i] = ord(ph[i])
        if ((1071 < ph[i] < 1104) == False) and ((1039 < ph[i] < 1072) == False):
            pass
        else:
            ph[i] = ph[i] + step
            if ph[i] > 1103 and flag == True:
                ph[i] = 1072 + (ph[i] - 1104)
            elif ph[i] > 1071 and flag == False:
                ph[i] = 1040 + (ph[i] - 1072)
        ph[i] = chr(ph[i])
    ph = "".join(ph)
    return ph


def caesar_decryption(phrase):
    flag = False
    i = 0
    while not flag:
        i += 1
        if i < 32:
            answer = input(f'ROT{numbers[i]}:{caesar_encryption(phrase, i)}\если код читаемый введите любой символ,  нет - нажмите Enter: ')
            if answer != '':
                flag = True
                return caesar_encryption(phrase, i)
        else:
            print('К сожалению, текст нельзя расшифровать')
            flag = True
            return ''


def vernam_encryption(phrase):
    global key
    key = input('чтобы ключ сгенерировался случайным образом нажмите Enter')
    if key == '' or len(key) != len(phrase):
        key = [chr(random.randint(32, 1500)) for i in range(len(phrase))]
    ph = list(phrase)
    k = list(key)
    answer = "".join([chr(ord(ph[i])^ord(k[i])) for i in range(len(ph))])
    return answer

def vernam_decryption(phrase):
    ph = list(phrase)
    k = list(key)
    answer = "".join([chr(ord(ph[i]) ^ ord(k[i])) for i in range(len(ph))])
    return answer


phrase1 = '''Шифр Цезаря.'''
phrase2 = '''Шифр Вернама '''

print(f'''Шифр Цезаря\nЗашифрованный текст:\n{caesar_encryption(phrase1)}\nРасшифровка текста:\n{caesar_decryption(caesar_encryption(phrase1))}''')
print(f'''Шифр Вернама\nЗашифрованный текст:\n{vernam_encryption(phrase2)}\nРасшифрованный текст:\n{vernam_decryption(vernam_encryption(phrase2))}''')
