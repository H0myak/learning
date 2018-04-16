#!/usr/bin/python3

import sys
import math
from datetime import datetime

password = ''
alphabet = "0123456789aAbCdEfHiJkLmNpqRtUvWxY"
random_number = str(datetime.utcnow().strftime('%f'))
help = "./random_generator.py -c <number of symbols in password> -n <number of string>"

def random(chain,number,password,alphabet,random_number):

	while len(random_number) < chain * number * 2:
		try:
			random_number = str(int(math.pow(int(random_number),2)))
		except:
			if chain > 1024:
				print ("ERROR! Max 1024 symbols in string. Aborted.")
				sys.exit(1)
			else:
				random_number = str(int(random_number + random_number) * 2)

	while int(random_number) >= 33:
		random_number = int(random_number)//33
		password += alphabet[random_number % 33]
	counter = n = 0
	while n < len(password):
		if len(password[n : n + chain]) < chain or counter == number:
			sys.exit(0)
		print (password[n : n + chain])
		n += chain
		counter += 1
	sys.exit(0)

try:
	print (str(sys.argv[1:]))
	for n in sys.argv[1:]:
		print (str(n))
		if sys.argv[n] == '-c':
			chain = 8 #int(sys.argv[n + 1])
#			n += 2
		elif sys.argv[n] == '-n':
			number = 5 #int(sys.argv[n + 1])
#			n += 2
		elif sys.argv[n] == '-h' or sys.argv[n] == '--help':
			print (help)
			sys.exit()
#		else:
#			n += 1
except:
	print(help)
	sys.exit(1)

random(chain,number,password,alphabet,random_number)
