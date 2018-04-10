#!/usr/bin/python3

import sys
import math
from datetime import datetime

random_number = str(datetime.utcnow().strftime('%f'))
chain = int(input ("Characters in string: "))
while len(random_number) < chain:
	try:
		random_number = str(int(math.pow(int(random_number),2)))
	except:
		if chain > 1024:
			print ("ERROR! Max 1024 symbols in string. Aborted.")
			sys.exit(1)
		else:
			random_number = str(int(random_number + random_number) * 2)
print (random_number[0:int(chain)])
sys.exit(0)
