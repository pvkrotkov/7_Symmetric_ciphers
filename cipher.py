
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
            answer = input(f'ROT{numbers[i]}:{caesar_encryption(phrase, i)}\nЕсли вы считаете, что этот текст можно прочитать введите любой символ, если же нет - просто нажмите Enter: ')
            if answer != '':
                flag = True
                return caesar_encryption(phrase, i)
        else:
            print('К сожалению, текст нельзя расшифровать, попробуйте другие шифры')
            flag = True
            return ''


def vernam_encryption(phrase):
    global key
    key = input('Если хотите введите ключ, чтобы ключ сгенерировался случайным образом нажмите Enter')
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


phrase1 = '''Шифр Цезаря, также известный как шифр сдвига, код Цезаря или сдвиг Цезаря — один из самых 
            простых и наиболее широко известных методов шифрования.'''
phrase2 = '''Шифр Вернама (англ. Vernam cipher) — система симметричного шифрования, изобретённая 
            в 1917 году Гилбертом Вернамом'''

print(f'''Шифр Цезаря\nЗашифрованный текст:\n{caesar_encryption(phrase1)}\nРасшифровка текста:\n{caesar_decryption(caesar_encryption(phrase1))}''')
print(f'''Шифр Вернама\nЗашифрованный текст:\n{vernam_encryption(phrase2)}\nРасшифрованный текст:\n{vernam_decryption(vernam_encryption(phrase2))}''')