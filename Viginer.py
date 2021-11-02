def encrypt(step, massive):
    global encrypted
    encrypted= ''
    step = [ord(i) for i in step]

    for j in range(len(massive)):

        crypting = ord(massive[j])
        crypting += step[j % len(step)]

        encrypted += chr(crypting % 65536)

    print('Зашифрованный вид исходного текста:')
    print(encrypted)
    return ''.join(encrypted)


def decrypt(step, massive):
    global decrypted
    decrypted = ''

    step = [ord(i) for i in step]

    for j in range(len(massive)):

        decrypting = ord(massive[j])
        decrypting -= step[j % len(step)]

        decrypted += chr(decrypting % 65536)
    return decrypted


frts_data = input('Введите текст для шифрования\n') # a i b sideli na trybe, a ypala b propala, kto ostalsya na trybe?
step = (input('Введите шаг шифрования\n'))

encrypt(step, frts_data)
print('Исходный текст:')
print(decrypt(step, encrypted))