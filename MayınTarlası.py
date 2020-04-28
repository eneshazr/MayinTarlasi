#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import random as r
import os
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

def giris():
	
	print('\n'*50)

	print(Fore.YELLOW + """
		+--------------------------------+
		|				 |
		|  	  MAYIN TARLASI V1	 |
		|				 |
		+--------------------------------+
 NOT:
 ilk 25'lik tarlada başlarsınız. Patlamadan gerekli sınıra ulaşırsan bir sonraki tarlaya eşekler eşliğinde gidersin.
 25'lik adım = 14
 50'lik adım = 25
 75'lik adım = 40
 100'lük adım = 60

 Patlarsan sıfırdan başlarsın haberin olsun!



		""")

def hata():	
	for i in range(4):
		print(Fore.RED + "!! BOMMM EŞEKLERLE TELEF OLDUN !!")
	print(Fore.RED + "!! ADIM VE LEVEL SIFIRLANDI !!\n| Devam Etmek için [evet] \n| Çıkmak için [exit] yaz.")
	print("\a")
	while True:
		giris = str(input("|: "))
		if giris == "evet":
			giris()
			yirmilik()
			print("Tekrardan Yirmilik Tarladasın!")
			continue
		if giris == "exit":
			for exit in range(1,4):
				time.sleep(1)
				print(exit)
			quit()
		else:
			print(Fore.RED + "HATALI SEÇENEK")
		
def yuzluk():
	os.system('cls' if os.name=='nt' else 'clear')
	puan = 0
	liste = []
	print(Fore.RED +"|  100 DÖNÜMLÜK TARLADASINIZ ! DİKKAT !  |")
	print(Fore.RED +"60 Doğru Adım Atmanız Gerekiyor..")
	while True:
		yuz = r.randint(1,101)
		try:
			if giris in liste:
				print("AYNI SAYIYI YAZAMAZSIN")
				continue
			else:
				liste.append(giris)
			giris = int(input(Fore.BLUE + "Tahmininiz: "))
			if giris == yuz:
				print(hata())			
			elif (giris <= 0 or giris >= 76):
				print(Fore.RED + "HATALI SAYI!")
				continue
			elif puan == 60:
				print("-"*53)
				print(Fore.RED +"|  Tebrikler! 100 Dönümlük Tarlayı Ölmeden Geçtiniz..  |")
				print(Fore.RED +"|  ARTIK ÖZGÜRSÜN !!")
				print(Fore.RED +"|  ~ Çıkış Yapılıyor... ~  |")
				for f in range(1,4):
					time.sleep(1)
					print(f)
					quit()
			elif giris != yuz:
				puan += 1
				print(Fore.GREEN +"+1 eklendi")
				print(Fore.GREEN +"Adımınız: "+ str(puan))
		except (ValueError, NameError, TypeError, RuntimeError, OSError, ZeroDivisionError):
			print(Fore.RED +"SADECE SAYI!")

def yetmislik():
	os.system('cls' if os.name=='nt' else 'clear')
	puan = 0
	liste = []
	print(Fore.RED +"|  75 DÖNÜMLÜK TARLADASINIZ ! DiKKAT !  |")
	print(Fore.RED +"40 Doğru Adım Atmanız Gerekiyor.")
	while True:
		yetmis = r.randint(1,76)
		try:
			if giris in liste:
				print("AYNI SAYIYI YAZAMAZSIN")
				continue
			else:
				liste.append(giris)
			giris = int(input(Fore.BLUE + "Tahmininiz: "))
			if giris == yetmis:
				print(hata())				
			elif (giris <= 0 or giris >= 76):
				print(Fore.RED + "HATALI SAYI!")
				continue
			elif puan == 40:
				print("-"*53)
				print(Fore.RED +"|  Tebrikler! 75 Dönümlük Tarlayı Ölmeden Geçtiniz..  |")
				print(Fore.RED +"|  Eşekler Bekleniyor...")
				for x in range(1):
					time.sleep(2)
					print(Fore.RED +"|  100 Dönümlük Tarlaya Eşeklerle Gidiliyor...  |")
				print("-"*53)
				for c in range(1,4):
					time.sleep(1)
					print(c)
				print('\n'*53)
				yuzluk()
			elif giris != yetmis:
				puan += 1
				print(Fore.GREEN +"+1 eklendi")
				print(Fore.GREEN +"Adımınız: "+ str(puan))
		except (ValueError, NameError, TypeError, RuntimeError, OSError, ZeroDivisionError):
			print(Fore.RED +"SADECE SAYI!")

def ellilik():
	os.system('cls' if os.name=='nt' else 'clear')
	puan = 0
	liste = []
	print(Fore.RED +"|  50 DÖNÜMLÜK TARLADASINIZ ! DİKKAT !  |")
	print(Fore.RED +"25 Doğru Adım Atmanız Gerekiyor.")
	while True:
		elli = r.randint(1,51)
		try:
			giris = int(input(Fore.BLUE + "Tahmininiz: "))
			if giris in liste:
				print("AYNI SAYIYI YAZAMAZSIN")
				continue
			else:
				liste.append(giris)
			if giris == elli:
				print(hata())				
			elif (giris <= 0 or giris >= 51):
				print(Fore.RED + "HATALI SAYI!")
				continue
			elif puan == 25:
				print("-"*53)
				print(Fore.RED +"|  Tebrikler! 25 Dönümlük Tarlayı Ölmeden Geçtiniz..  |")
				print(Fore.RED +"|  Eşekler Bekleniyor...")
				for x in range(1):
					time.sleep(2)
					print(Fore.RED +"|  75 Dönümlük Tarlaya Eşeklerle Gidiliyor...  |")
				print("-"*53)
				for c in range(1,4):
					time.sleep(1)
					print(c)
				print('\n'*53)
				yetmislik()
			elif giris != elli:
				puan += 1
				print(Fore.GREEN +"+1 eklendi")
				print(Fore.GREEN +"Adımınız: "+ str(puan))
		except (ValueError, NameError, TypeError, RuntimeError, OSError, ZeroDivisionError):
			print(Fore.RED +"SADECE SAYI!")

def yirmilik():
	puan = 0
	liste = []
	while True:
		yirmi = r.randint(1,26)
		try:
			giris = int(input(Fore.BLUE + "Tahmininiz: "))
			if giris in liste:
				print("AYNI SAYIYI YAZAMAZSIN")
				continue
			else:
				liste.append(giris)
			if giris == yirmi:
				print(hata())
			elif (giris <= 0 or giris >= 26):
				print(Fore.RED + "HATALI SAYI!")
				continue
			elif puan == 13:
				print("-"*53)
				print(Fore.RED +"|  Tebrikler! 25 Dönümlük Tarlayı Ölmeden Geçtiniz..  |")
				print(Fore.RED +"|  Eşekler bekleniyor...")
				for x in range(1):
					time.sleep(2)
					print(Fore.RED +"|  50 Dönümlük Tarlaya Eşeklerle Gidiliyor...  |")
				print("-"*53)
				for c in range(1,4):
					time.sleep(1)
					print(c)
				print('\n'*53)
				ellilik()
			elif giris != yirmi:
				puan += 1
				print(Fore.GREEN +"+1 eklendi")
				print(Fore.GREEN +"Adımınız: "+ str(puan))

		except (ValueError, NameError, TypeError, RuntimeError, OSError, ZeroDivisionError):
			print(Fore.RED +"SADECE SAYI!")
giris()
yirmilik()
