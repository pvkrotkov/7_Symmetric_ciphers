from collections import Counter

def caesar(text, shift, type):
    return ''.join(map(chr, [(x + shift) % 65536 if type == 'encrypt' else (x - shift) % 65536 for x in map(ord, text)]))

def no_key(text):
    return caesar(text, ord(Counter(text).most_common()[0][0]) - ord(' '), 'decrypt')

def vigenere(message, key, type):
    encrypted = ""
    split_message = [message[i : i + len(key)] for i in range(0, len(message), len(key))]
    for each_split in split_message:
        i = 0
        for letter in each_split:
            if type == 'encrypt':
                number = (letter_to_index[letter] + letter_to_index[key[i]]) % len(alphabet)
            else:
                number = (letter_to_index[letter] - letter_to_index[key[i]]) % len(alphabet)
            encrypted += index_to_letter[number]
            i += 1
    return encrypted


cipher = input('Cipher? Type "caesar" or "vigenere": ')

if cipher == "caesar":
    decrypted_text = "Hello, world! This text is encrypted.$" #normal
    encrypted_text = 'Mjqqt1%|twqi&%Ymnx%yj}y%nx%jshw~uyji3)' #encrypted
    key = 5
    print("\n=======================EXAMPLE=======================\n")
    print("ecnrypted: ", caesar(decrypted_text, int(key), 'encrypt'))
    print("decrypted: ", caesar(encrypted_text, int(key), 'decrypt'))
    print("this text was decrypted with no key: ", no_key(encrypted_text))
    print("\n=====================================================\n")
    while True:
        a = input('What do you want? Type "encrypt" or "decrypt": ')
        if a != "encrypt" and a != "decrypt":
            print('invalid input')
            continue
        b = input('Type text: ')
        c = input('Enter the key between 1 and 25: ')
        try:
            if int(c) < 1 or int(c) > 25:
                print('invalid input')
                continue
        except:
            print('invalid input')
            continue
        break

    if a == "encrypt":
        print('normal text: ', b)
        print('encrypted text: ', caesar(b, int(c), 'encrypt'))
    else:
        print('encrypted text: ', b)
        print('normal text: ', caesar(b, int(c), 'decrypt'))
elif cipher == "vigenere":
    alphabet = "abcdefghijklmnopqrstuvwxyz.-=,!\\|/$%@#!;'>?<&*+-)_(№`~01234:^56789 ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letter_to_index = dict(zip(alphabet, range(len(alphabet))))
    index_to_letter = dict(zip(range(len(alphabet)), alphabet))

    decrypted_text = "This is encrypted text! 1$ = 71,66 RUB; Today is 03/11/2021; _#python3; @example" #normal
    encrypted_text = "UhvsMit rnprzp|eq ue@t№ 2$M=M72,I6MRVB` goea# vsA0D/B1$2A2B;A_(p#tio.3` #e@azpme" #e@azpme' #encrypted
    key = 'banana'

    print("\n=======================EXAMPLE=======================\n")
    print("ecnrypted: ", vigenere(decrypted_text, key, 'encrypt'))
    print("decrypted: ", vigenere(encrypted_text, key, 'decrypt'))
    print("\n=====================================================\n")

    while True:
        a = input('What do you want? Type "encrypt" or "decrypt": ')
        if a != "encrypt" and a != "decrypt":
            print('invalid input')
            continue
        b = input('Type text: ')
        c = input('Enter the key: ')
        break

    if a == "encrypt":
        print('\nnormal text: ', b)
        print('encrypted text: ', vigenere(b, c, 'encrypt'), '\n')
    else:
        print('\nencrypted text: ', b)
        print('normal text: ', vigenere(b, c, 'decrypt'), '\n')

else:
    print('invalid input')
