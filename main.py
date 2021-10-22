from random import randint
from Cipher import Caesar, Vernam


def main():
    key = randint(1, 100)
    message = input("Введите сообщение:\n")

    print("Цифр Цезаря")
    caesar = Caesar(key)
    encrypted_message = caesar.encrypt(message)
    print("\nЗашифрованный текст")
    print(encrypted_message)
    decrypted_message = caesar.decrypt(encrypted_message)
    print("\nРасшифрованный текст")
    print(decrypted_message)
    print("\nВзломанный текст")
    print(caesar.hack(encrypted_message), "\n")

    print("Цифр Вернама")
    vernam = Vernam(key)
    encrypted_message = vernam.encrypt(message)
    print("\nЗашифрованный текст")
    print(encrypted_message)
    encrypted_message = vernam.decrypt(encrypted_message)
    print("\nРасшифрованный текст")
    print(encrypted_message)


if __name__ == '__main__':
    main()
