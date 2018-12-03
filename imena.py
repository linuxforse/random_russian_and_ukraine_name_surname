#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import random
mansi = "imena_m.txt"
mansf = "family_m.txt"
womani = "imena_f.txt"
womanf = "family_f.txt"


def imfaot(ci,cf):

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
	a = ""
	b = ""
	a = line[rand]
	b = fam[famrand]
	a = a.rstrip("\n")
	b = b.rstrip("\n")
	a = a.capitalize()
	b = b.capitalize()
	return (a,b)

if len(sys.argv) <= 1:
	print("Введите -m или -f")
elif sys.argv[1] == "-m":
	ci = mansi
	cf = mansf
elif sys.argv[1] == "-f":
	ci = womani
	cf = womanf
else:
	print("Неправильный аргумент командной строки")

imret, famret = imfaot(ci,cf)
print(imret)
print(famret)


