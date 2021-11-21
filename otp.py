from binascii import hexlify, unhexlify
def shifr(shifrovka, key):
    cipher = xor_str(shifrovka, key)
    return (hexlify(cipher.encode())).decode()

def deshifr(shifrovka, key):
    shifrovka = (unhexlify(shifrovka.encode())).decode()
    return xor_str(shifrovka, key)
from itertools import cycle

def xor_str(a, b):
    return ''.join([chr(ord(x)^ord(y)) for x, y in zip(a, cycle(b))])


from random import randint

def gener_key(lenn):
    key=''
    for i in range (lenn):
        #num=
        key+=chr(randint(0, 6555))
        #print(num, key)
    return(key)

shifrovka="Владимиров — Исаев — Штирлиц родился 8 октября 1900 года («Экспансия — I») в Забайкалье, где его родители находились в политической ссылке. Если верить самому Штирлицу, то какое-то время в детстве он провёл в окрестностях старинного русского городка Гороховца. Юлиан Семёнов не говорит о том, что его герой родился здесь: «Штирлиц понял, что его тянуло именно к этому озеру, оттого, что вырос он на Волге, возле Гороховца, где были точно такие же жёлто-голубые сосны». Сам Гороховец стоит на реке Клязьме, и до Волги от него далеко. Но Исаев мог провести детство «на Волге близ Гороховца», поскольку существовавший в то время Гороховецкий уезд был в 4 раза больше нынешнего Гороховецкого района и в северной части доходил до Волги."
key = gener_key(len(shifrovka))
shifrovanue = False
vuvod=''
while True:
    print("\n",shifrovka)
    print("\n","-"*20, "\n")
    print('Текущее шифрование осуществляется по ключу: ', key,"\n", vuvod)
    vuvod=''
    komm=input('exit - выход, cngtxt - подменить расшифровку (ввод не шифрованного), cngsh - подменить шифровку, key - изменить ключ, Alex - зашифровать, Ustas - дешифровать, genkey - сгенерировать новый ключ: ')
    if komm== 'exit':
        print('Штирлиц, а вас я попрошу остаться')
        break
    elif komm== 'cngtxt':
        shifrovka=input('Что передаёт радистка Кэт?: ')
        shifrovanue = False
    elif komm== 'cngsh':
        shifrovka=input('Какую шифровку нужно доставить в Швейцарию? (Ключ может быть сброшен): ')
        shifrovanue = True
        if len(key)!=len(shifrovka):
            key = False
    elif komm== 'key' and shifrovanue==False:
        try:
            nkey = input('Задать смещение: ')
            if len(nkey)==len(shifrovka):
                key=nkey
            else:
                raise ValueError
        except:
            vuvod='Длина кода должна равняться длине шифровки'
    elif komm== 'Alex' and shifrovanue==False and key:
        shifrovanue=True
        shifrovka= shifr(key, shifrovka)
    elif komm== 'Ustas' and shifrovanue and key:
        shifrovka= deshifr(shifrovka, key)
        shifrovanue=False
    elif komm== 'genkey':
        key=gener_key(len(shifrovka))
    elif (komm== 'key' or komm== 'Alex') and shifrovanue:
        vuvod='Сперва дешифруйте текст'
    elif(komm== 'Ustas' or komm== 'Bronevoy') and shifrovanue==False:
        vuvod='Сперва зашифруйте текст'
    elif (komm== 'Ustas' or komm==  'Alex') and key == False:
        print('Сперва задайте или взломайте смещение')
    else:
        vuvod='Не понял вас. Повторите, пожалуйста'
