#!/usr/bin/python3

import sys
import math
import getopt
from datetime import datetime

def main (argv):
	password = ''
	alphabet = "0123456789aAbCdEfHiJkLmNpqRtUvWxY"
	random_number = str(datetime.utcnow().strftime('%f'))
	help_message = "./random_generator.py -c <number of symbols in password> -n <number of string>"

	try:
		opts, args = getopt.getopt(argv,"hc:n:",["chain=", "number="])
	except:
		print (help_message)
		sys.exit(1)

	for opt,arg in opts:
		if opt=='-h':
			print (help_message)
			sys.exit()
		elif opt in ("-c","--chain"):
			chain = int(arg)
		elif opt in ("-n","--number"):
			number = int(arg)	
	random(chain,number,password,alphabet,random_number)
	
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

if __name__ == "__main__":
	main(sys.argv[1:])