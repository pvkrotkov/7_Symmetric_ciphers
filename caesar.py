def shifr(k, text):
    
    return ''.join(map(chr, [(x + k) % 65535 for x in map(ord, text)]))


def deshifr(k, text):
    return ''.join(map(chr, [(x - k) % 65535 for x in map(ord, text)]))

def vzlom(p):
    #'''
    spicok = {}
    
    for i in p:
        if i in spicok:
            spicok[i] += 1
        else:
            spicok.update({i:1})
    max_kol=0
    max_bukv=''
    for i in spicok:
        if spicok[i] > max_kol:
            max_kol=spicok[i]
            max_bukv=i
    key = ord(max_bukv) - ord(' ')
    return key#'''


shifrovka="Владимиров — Исаев — Штирлиц родился 8 октября 1900 года («Экспансия — I») в Забайкалье, где его родители находились в политической ссылке. Если верить самому Штирлицу, то какое-то время в детстве он провёл в окрестностях старинного русского городка Гороховца. Юлиан Семёнов не говорит о том, что его герой родился здесь: «Штирлиц понял, что его тянуло именно к этому озеру, оттого, что вырос он на Волге, возле Гороховца, где были точно такие же жёлто-голубые сосны». Сам Гороховец стоит на реке Клязьме, и до Волги от него далеко. Но Исаев мог провести детство «на Волге близ Гороховца», поскольку существовавший в то время Гороховецкий уезд был в 4 раза больше нынешнего Гороховецкого района и в северной части доходил до Волги."
key = 17
shifrovanue = False
vuvod=''
while True:
    print("\n",shifrovka)
    print("\n","-"*20, "\n")
    print('Текущее шифрование осуществляется по смещению', key,"\n", vuvod)
    vuvod=''
    komm=input('exit - выход, cngtxt - подменить расшифровку (ввод не шифрованного), cngsh - подменить шифровку (ввод шифрованного текста. Смещение НЕ изменится автоматом), key - изменить смещение, Alex - зашифровать, Ustas - дешифровать по заданному смещению, Bronevoy - взломать смещение шифровки, delkey - удалить смещение: ')
    if komm== 'exit':
        print('Штирлиц, а вас я попрошу остаться')
        break
    elif komm== 'cngtxt':
        shifrovka=input('Что передаёт радистка Кэт?: ')
        shifrovanue = False
    elif komm== 'cngsh':
        shifrovka=input('Какую шифровку нужно доставить в Швейцарию?: ')
        shifrovanue = True
    elif komm== 'key' and shifrovanue==False:
        try:
            nkey = input('Задать смещение: ')
            if float(nkey) == int(nkey) and int(nkey)!=0:
                key=int(nkey)
            else:
                raise ValueError
        except:
            vuvod='Смещение должно быть задано целой цифрой и не равняться 0'
    elif komm== 'Alex' and shifrovanue==False and key:
        shifrovanue=True
        shifrovka= shifr(key, shifrovka)
    elif komm== 'Ustas' and shifrovanue and key:
        shifrovanue=False
        shifrovka= deshifr(key, shifrovka)
    elif komm== 'Bronevoy' and shifrovanue:
        key = vzlom(shifrovka)
        vuvod="Смещение = "+str(key)
    elif komm== 'delkey':
        key=False
    elif (komm== 'key' or komm== 'Alex') and shifrovanue:
        vuvod='Сперва дешифруйте текст'
    elif(komm== 'Ustas' or komm== 'Bronevoy') and shifrovanue==False:
        vuvod='Сперва зашифруйте текст'
    elif (komm== 'Ustas' or komm==  'Alex') and key == False:
        print('Сперва задайте или взломайте смещение')
    else:
        vuvod='Не понял вас. Повторите, пожалуйста'