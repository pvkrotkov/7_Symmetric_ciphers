def fst(L,R,keyi, N, key):
    d_key=len(key)
    for i in range(N):
        K = ord(key[keyi % d_key::][0])
        temp = R ^ (L ^ K)
        R = L
        L = temp
        keyi += 1
    end = (chr(R) + chr(L))
    return end,keyi

def fst_decript(L,R, keyi, N, key):
    d_key=len(key)
    for i in range(N):
        K = ord(key[keyi % d_key::][0])
        temp = R ^ (L ^ K)
        R = L
        L = temp
        keyi -= 1
    end = (chr(L) + chr(R))
    return end,keyi
def razbivka (shifrovka):
    text=[]
    dlina = len(shifrovka)
    for i in range(0, dlina, 2):
        text.append(shifrovka[i:i + 2])#'''
    return(text)#, dlina//2)

def shifr(shifrovka, key, N):
    keyi = 0
    text = []
    if len(shifrovka) % 2 != 0 :
        shifrovka = shifrovka +' '
    shifrovka=razbivka (shifrovka)
    for x in shifrovka:
        elem,keyi = fst(ord(x[0]), ord(x[1]), keyi, N, key)

        text.append(elem)
    return(''.join(text))
def defshifr(shifrovka, key, N):
    shifrovka=razbivka (shifrovka)
    keyi = N*len(shifrovka)-1
    text=[]
    for x in shifrovka[::-1]:
        elem,keyi = fst_decript(ord(x[0]), ord(x[1]), keyi, N, key)
        text.append(elem)
    return(''.join(text)[::-1])
from random import randint
def gener_key(lenn):
    key=''
    for i in range (lenn):
        key+=chr(randint(0, 6555))
    return(key)














shifrovka="Владимиров — Исаев — Штирлиц родился 8 октября 1900 года («Экспансия — I») в Забайкалье, где его родители находились в политической ссылке. Если верить самому Штирлицу, то какое-то время в детстве он провёл в окрестностях старинного русского городка Гороховца. Юлиан Семёнов не говорит о том, что его герой родился здесь: «Штирлиц понял, что его тянуло именно к этому озеру, оттого, что вырос он на Волге, возле Гороховца, где были точно такие же жёлто-голубые сосны». Сам Гороховец стоит на реке Клязьме, и до Волги от него далеко. Но Исаев мог провести детство «на Волге близ Гороховца», поскольку существовавший в то время Гороховецкий уезд был в 4 раза больше нынешнего Гороховецкого района и в северной части доходил до Волги."
N=17
key = 'Мгновения'
shifrovanue = False
vuvod=''
while True:
    print("\n",shifrovka)
    print("\n","-"*20, "\n")
    print('Kоличество раундов в выбранном алгоритме шифрования:',N,"\n",'Текущее шифрование осуществляется по ключу: ', key,"\n", vuvod)
    vuvod=''
    komm=input('exit - выход, N - задать количество раундов, cngtxt - подменить расшифровку (ввод не шифрованного), cngsh - подменить шифровку, key - изменить ключ, Alex - зашифровать, Ustas - дешифровать, genkey - сгенерировать новый ключ: ')
    if komm== 'exit':
        print('Штирлиц, а вас я попрошу остаться')
        break
    elif komm== 'cngtxt':
        shifrovka=input('Что передаёт радистка Кэт?: ')
        shifrovanue = False
    elif komm== 'cngsh':
        shifrovka=input('Какую шифровку нужно доставить в Швейцарию?: ')
        shifrovanue = True
    elif komm== 'N' and shifrovanue==False:
        try:
            nkey = input('Задать кол-во раундов: ')
            if nkey.isdigit():
                N=int(nkey)
            else:
                raise ValueError
        except:
            vuvod='Кол-во раундов должно быть задано целой цифрой и быть больше 0'
    elif komm== 'key' and shifrovanue==False:
        nkey = input('Задать ключ: ')
        if nkey == '':
            vuvod='Ключ не должен быть пустым'
        else:
            key=nkey
    elif komm== 'Alex' and shifrovanue==False:
        shifrovanue=True
        shifrovka=shifr(shifrovka, key, N)
    elif komm== 'Ustas' and shifrovanue:
        shifrovka=defshifr(shifrovka, key, N)
        shifrovanue=False
    elif komm== 'genkey':
        try:
            nkey = input('Задать длину ключа: ')
            if float(nkey) == int(nkey) and int(nkey)>0:
                key=gener_key(int(nkey))
            else:
                raise ValueError
        except:
            vuvod='Длина должна быть задана целой цифрой и быть больше 0'
    elif (komm== 'key' or komm== 'Alex') and shifrovanue:
        vuvod='Сперва дешифруйте текст'
    elif(komm== 'Ustas' or komm== 'Bronevoy') and shifrovanue==False:
        vuvod='Сперва зашифруйте текст'
    elif komm== 'Ustas' or komm==  'Alex':
        print('Сперва задайте или взломайте смещение')
    else:
        vuvod='Не понял вас. Повторите, пожалуйста'
