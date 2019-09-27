#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import random
mansi = "imena_m.txt"
mansf = "family_m.txt"
womani = "imena_f.txt"
womanf = "family_f.txt"
mansotch = "otch_m_ru.txt"
womanotch = "otch_f_ru.txt"


def imfaot(ci,cf,co):

	f = open(ci,"r")
	line = f.readlines()
	lenline = len(line)
	rand = random.randint(0,lenline)
	f.close()

	r = open(cf,"r")
	fam = r.readlines()
	lenfam = len(fam)
	famrand = random.randint(0,lenfam)
	r.close()

	k = open(co,"r")
	ot = k.readlines()
	lenotch = len(ot)
	otchrand = random.randint(0,lenotch)
	k.close()	

	a = ""
	b = ""
	c = ""
	a = line[rand]
	b = fam[famrand]
	c = ot[otchrand]
	a = a.rstrip("\n")
	b = b.rstrip("\n")
	c = c.rstrip("\n")
	


	return (a,b,c)

def training():
	if len(sys.argv) <= 1:
		print("Введите -m или -f")
	elif sys.argv[1] == "-m":
		ci = mansi
		cf = mansf
		co = mansotch
		imret, famret, otchmret = imfaot(ci,cf,co)
		print(imret)
		print(otchmret)
		print(famret)

	elif sys.argv[1] == "-f":
		ci = womani
		cf = womanf
		co = womanotch

		imret, famret, otchmret = imfaot(ci,cf,co)
		print(imret)
		print(otchmret)
		print(famret)
	else:
		print("Неправильный аргумент командной строки")

	
	return 0

training()


