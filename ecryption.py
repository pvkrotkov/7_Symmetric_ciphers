from random import randint


alfavit =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'



def ceaser(message):
    smeshenie = int(input('Шаг шифровки: '))    #Создаем переменную с шагом шифровки
    mess = message.upper()    #создаем переменнную, куда запишем наше сообщение
    itog = ''    #создаем переменную для вывода итогового сообщения
    for i in mess:
        mesto = alfavit.find(i)    #Вычисляем места символов в списке
        new_mesto = mesto + smeshenie    #Сдвигаем символы на указанный в переменной smeshenie шаг
    for i in mess:
        mesto = alfavit.find(i)
        new_mesto = mesto + smeshenie
        if i in alfavit:
            itog += alfavit[new_mesto]  # Задаем значения в итог
        else:
            itog += i
    print (itog)

#ceaser('Hello')


def decript_ceasar(message):
    shift = int(input('Шаг шифровки: '))
    encrypted_text = message
    plain_text = ""
    for c in encrypted_text:
        # проверить, является ли символ заглавной буквой
        if c.isupper():
            c_index = ord(c) - ord("A")
            # выполнить отрицательный сдвиг
            new_index = (c_index - shift) % 26
            # преобразовать в новый символ
            new_unicode = new_index + ord("A")
            new_character = chr(new_unicode)
            # добавление к простой строке
            plain_text = plain_text + new_character
        else:
            # так как символ не является строчным, оставьте его как есть
            plain_text += c
    print("Расшифровано",plain_text)

#decript_ceasar('KHOOR')


def vijiner(message):
    key=''
    keys=''
    final=''
    mes = message
    for symbol in mes:
        key = randint(0,32); keys += str(key) + "/"
        final += chr((ord(symbol) + key - 17)%33 + ord('А'))
    print('Зашифрованное сообщение: ', final)
    print ('Ключ шифрования: ',keys)

#vijiner('Hello')
