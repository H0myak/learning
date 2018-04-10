import sys
from datetime import datetime

try:
	interface = raw_input ("[*] Enter Desired Inteface: ")
	ips = raw_input ("[*] Enter Range of IPs to Scan for: ")
except KeyboardInterrupt:
	print ("\n[*] User Requested Shutdown")
	print ("[*] Quitting...")
	sys.exit(1)

print ("\n[*] Scanning...")
start_time = datetime.now()

from scapy.all import srp,Ether,ARP,conf

conf.verb = 0
ans, unans = srp(Ether(sdt="ff:ff:ff:ff:ff:ff")/ARP(pdst = ips), timeout = 2, iface = interface,inter=0.1)

print ("MAC -IP\n")
for snd, rcv in ans:
	print (rcv.sprintf (r"%Ether.src% - %ARP.psrc%"))
stop_time = datetime.now()
print ("\n[*] Scan Complite!")
print ("[*] Scan Duration: %s" %(total_time))

