
import random
import string

def key_generator():
	alpha_list = [i for i in range(65,91)]
	k = []
	for i in range(26):
		k.append(random.choice(alpha_list))
		alpha_list.remove(k[len(k)-1])

	return k

def enc():
	plain_text = list(''.join(input().translate(str.maketrans('', '', string.punctuation)).upper().split())) #https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string
	cipher_text = []

	key = key_generator()
	for i in plain_text:
		cipher_text.append(chr(key[ord(i)-65]))

	print(key)
	print(''.join(cipher_text))

	# print('\n**Alphabet ASCII**')
	# a=[]
	# for i in string.ascii_uppercase:
	# 	a.append(i)
	# 	a.append(ord(i))
	# print(a)

# abcdefjhijklmnopqrstuvwxyz
enc()