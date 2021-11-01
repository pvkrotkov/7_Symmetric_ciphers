from collections import Counter
from random import *

#ceaser encryption function using unicodes of letters
def ceaser_encryption(shift, text):
	unicodes_of_letters = list(map(ord, text))
	shifted_unicodes = [uni + shift for uni in unicodes_of_letters]
	shifted_letters = list(map(chr, shifted_unicodes))
	res = ''.join(shifted_letters)
	return res

#ceaser decryption function using unicodes of letters
def ceaser_decryption(shift, text):
	unicodes_of_letters = list(map(ord, text))
	shifted_unicodes = [uni - shift for uni in unicodes_of_letters]
	list_of_shifted_letters = list(map(chr, shifted_unicodes))
	res = ''.join(list_of_shifted_letters)
	return res

#ceaser hack knowing that the most common is space
def hack_ceaser(text):
	space_unicode = ord(' ')

	def find_most_common(text):
		lst = Counter(text)
		symb_amount = lst.most_common(1)
		symb = symb_amount[0][0]
		return ord(symb)

	uni_of_most_common_symbol = find_most_common(text)
	shift = abs(space_unicode - uni_of_most_common_symbol)
	res = ceaser_decryption(shift, text)
	return res

#function that crypts with the power of the shift
def xor(symbol, shift):
    return chr(ord(symbol)^shift)

#vernama encryption, new key for each symbol
def vernama_encryption(text):
    shift = [randint(0,26) for _ in range(len(text))]
    encrypted_text = ''.join([xor(text[i], shift[i]) for i in range(len(text))])
    return encrypted_text , shift

#vernama decryption
def vernama_decryption(text, shift):
	decrypted = ''.join([xor(text[i], shift[i]) for i in range(len(text))])
	return decrypted

def main():
	print(ceaser_encryption(3, 'Hello!'))
	print(ceaser_decryption(3, 'Khoor$'))
	print('-'*50)
	text = 'he is a random guy that is wondering around my house lol'
	print(f'Original text: {text}')
	print('-'*50)
	crypted1 = ceaser_encryption(2, text)
	print(f'Encrypted text (ceaser): {crypted1}')
	print(f'Decrypted text (ceaser): {hack_ceaser(crypted1)}')
	print('-'*50)
	crypted2, shift = vernama_encryption('he is a random guy that is wondering around my house lol')
	print(f'Encrypted text (vernama): {crypted2}')
	print(f'Decrypted text (vernama): {vernama_decryption(crypted2, shift)}')

if __name__=='__main__':
	main()
