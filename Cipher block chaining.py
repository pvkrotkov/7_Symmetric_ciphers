from binascii import hexlify, unhexlify
def shifr_c(shifrovka, key):
    shifrovka = xor_str(shifrovka, key)
    return (hexlify(shifrovka.encode())).decode()


from itertools import cycle

def xor_str(a, b):
    return ''.join([chr(ord(x)^ord(y)) for x, y in zip(a, cycle(b))])

#def

def deshifr_C(shifrovka, key, dlin):
    shifrovka = (unhexlify(shifrovka.encode())).decode()
    text=[]
    while shifrovka != '':
        i=1
        nkey =''
        #print(''.join(text), key)
        for x, y in zip(shifrovka, cycle(key)):
            #print(x, y)
            text.append(chr(ord(x)^ord(y))) 
            if i < dlin:
                i+=1
                nkey+=x
            else:
                #print(99, ''.join(text)[-dlin:], key, nkey, nkey+x)
                #input()
                key=shifr_c(''.join(text)[-dlin:], key)
                #input(str(key))
                shifrovka=shifrovka[dlin:]
                break
    #return xor_str(shifrovka, key)
    return(''.join(text))

from random import randint

def gener_key(lenn):
    key=''
    for i in range (lenn):
        key+=chr(randint(0, 6555))
    return(key)



def vizjg(key, shifrovka):
    ltxt=len(shifrovka)
    key_l=len(key)
    text=[]
    for i in range (ltxt):
        text.append((ord(shifrovka[i]) ^ ord(key[i%key_l])) % 65535)
    return ''.join(map(chr, text))


def alexa (shifrovka, vect, key):
    text=[]
    db=len(vect)
    d=len(shifrovka)//db
    for i in range (d):
        vect=shifr_c(shifrovka[:db], vect)
        shifrovka=shifrovka[db:]
        text.append(vect)
    text.append(shifrovka)
    return(vizjg(key, ''.join(text)))
def ustas (key, shifrovka, blo):
    return(deshifr_C(vizjg(key, shifrovka), blo, len(blo)))

shifrovka="Владимиров — Исаев — Штирлиц родился 8 октября 1900  года в Забайкалье, где его родители находились в политической ссылке. Если верить самому Штирлицу, то какое-то время в детстве он провёл в окрестностях старинного русского городка Гороховца. Юлиан Семёнов не говорит о том, что его герой родился здесь: «Штирлиц понял, что его тянуло именно к этому озеру, оттого, что вырос он на Волге, возле Гороховца, где были точно такие же жёлто-голубые сосны». Сам Гороховец стоит на реке Клязьме, и до Волги от него далеко. Но Исаев мог провести детство «на Волге близ Гороховца», поскольку существовавший в то время Гороховецкий уезд был в 4 раза больше нынешнего Гороховецкого района и в северной части доходил до Волги."
key = 'Мгновения'
blo=gener_key(7)
db=7
shifrovanue = False
vuvod=''
while True:
    print("\n",shifrovka)
    print("\n","-"*20, "\n")
    print('Текущий вектор:', blo,"\n",'Длина шифровки:', len(shifrovka),"\n", 'Текущее шифрование осуществляется по смещению', key,"\n", vuvod)
    vuvod=''
    komm=input('exit - выход, cngtxt - подменить расшифровку (ввод не шифрованного), cngsh - подменить шифровку, key - изменить ключ, vec - ввести новый вектор, Alex - зашифровать, Ustas - дешифровать, genvec - сгенерировать новый вектор: ')
    if komm== 'exit':
        print('Штирлиц, а вас я попрошу остаться')
        break
    elif komm== "genvec" and shifrovanue==False:
        try:
            nkey = input('Задать длину вектора: ')
            if float(nkey) == int(nkey) and int(nkey)>0 and len(shifrovka)%int(nkey)==0:
                blo=gener_key(int(nkey))
                db=nkey
            else:
                raise ValueError
        except:
            vuvod='Длина должна быть задана целой цифрой и быть больше 0'
    elif komm== 'vec' and shifrovanue==False:
        nkey = input('Задать вектор: ')
        if nkey == '':
            print('Вектор не должен быть пустым')
        elif len(shifrovka)%len(nkey)>0:
            print('Шифровка должна делиться на вектор')
        else:
            blo=nkey
            db=len(blo)
    elif komm== 'cngtxt':
        shifrovka=input('Что передаёт радистка Кэт?: ')
        shifrovanue = False
        blo = False
    elif komm== 'cngsh':
        shifrovka=input('Какую шифровку нужно доставить в Швейцарию?: ')
        shifrovanue = True
        blo=False
    elif komm== 'key' and shifrovanue==False:
            nkey = input('Задать код: ')
            if nkey == '':
                print('Код не должен быть пустым')
            else:
                key=nkey
    elif komm== 'Alex' and shifrovanue==False and key:
        #
        #'''
        shifrovanue=True
        shifrovka=alexa(shifrovka, blo, key)
    elif komm== 'Ustas' and shifrovanue and key:
        shifrovka=ustas (key, shifrovka, blo)
        shifrovanue=False
    elif komm== 'delkey':
        key=False
    elif (komm== 'key' or komm== 'Alex' or komm== "genvec" or komm== "vec") and shifrovanue:
        vuvod='Сперва дешифруйте текст'
    elif (komm== 'Ustas') and shifrovanue==False:
        vuvod='Сперва зашифруйте текст'
    elif (komm== 'Ustas' or komm==  'Alex') and key == False:
        vuvod=('Сперва задайте или взломайте смещение')
    elif key==False and komm== 'Ustas':
        vuvod='Введите или взломайте смещение'
    else:
        vuvod='Не понял вас. Повторите, пожалуйста'