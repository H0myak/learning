#!/usr/bin/python3

import sys
import math
from datetime import datetime

password = ''
alphabet = "0123456789aAbCdEfHiJkLmNpqRtUvWxY"

random_number = str(datetime.utcnow().strftime('%f'))

chain = int(input ("Characters in string: "))
number = int(input ("Number of passwords: "))

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

n = 0
while n < len(password):
	if len(password[n : n + chain]) < chain:
		sys.exit(0)
	print (password[n : n + chain])
	n += chain

sys.exit(0)
