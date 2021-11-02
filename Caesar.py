def encrypt(step, massive):
    global encrypted
    encrypted=''.join(map(chr, [x + step for x in map(ord, massive)]))
    print('Зашифрованный вид исходного текста:')
    print(encrypted)
    return encrypted

def decrypt_with_step(step, massive):
    return ''.join(map(chr, [x - step for x in map(ord, massive)]))
    

def analysis(encrypted):
    global key

    empty_dict = {}
    empty_lst = []
    tmp_lst = []

    print(f'Количество всех символов:{len(encrypted)}\n')

    for i in encrypted:
        if i not in empty_lst:
            empty_lst.append(i)
            
    for i in empty_lst:
        tmp_lst.append([i,0])

    for i in tmp_lst:
        empty_dict.update([i])

    print(f'Количество уникальных символов {len(empty_dict)}\n')

    for i in encrypted:
        empty_dict[i]+=1

    max_val=max(empty_dict.values())

    for key, v in empty_dict.items(): 
        if v == max_val:
            print(f'Возможный символ, заменяющий пробел:\n{key}')
            return(key)
    

def decrypt_without_step(encrypted):
    tmp_val = ord(key) - 32
    return ''.join(map(chr, [x - tmp_val for x in map(ord, encrypted)]))


frts_data = input('Введите текст для шифрования\n') # a i b sideli na trybe, a ypala b propala, kto ostalsya na trybe?
step = int(input('Введите шаг шифрования\n'))



encrypt(step, frts_data)
analysis(encrypted)
print('Исходный текст:')
print(decrypt_without_step(encrypted))


#print(decrypt_with_step(step, encrypted ))
