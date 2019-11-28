#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import random




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


	if rand > 0:
		rand-=1
	if famrand > 0:
		famrand-=1
	if otchrand > 0:
		otchrand-=1

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
	elif sys.argv[1] == "-m" and sys.argv[2] == "-ru":
		mansiru = "imena_m_ru.txt"
		mansfru = "family_m_ru.txt"
		mansotchru = "otch_m_ru.txt"

		ci = mansiru
		cf = mansfru
		co = mansotchru
		imret, famret, otchmret = imfaot(ci,cf,co)
		print(imret)
		print(otchmret)
		print(famret)

	elif sys.argv[1] == "-f" and sys.argv[2] == "-ru":
		womaniru = "imena_f_ru.txt"
		womanfru = "family_f_ru.txt"
		womanotchru = "otch_f_ru.txt"

		ci = womaniru
		cf = womanfru
		co = womanotchru

		imret, famret, otchmret = imfaot(ci,cf,co)
		print(imret)
		print(otchmret)
		print(famret)

	elif sys.argv[1] == "-m" and sys.argv[2] == "-ua":
		mansiua = "imena_m_ua.txt"
		mansfua = "family_m_ua.txt"
		mansotchua = "otch_m_ua.txt"

		ci = mansiua
		cf = mansfua
		co = mansotchua
		imret, famret, otchmret = imfaot(ci,cf,co)
		print(imret)
		print(otchmret)
		print(famret)

	elif sys.argv[1] == "-f" and sys.argv[2] == "-ua":
		womaniua = "imena_f_ua.txt"
		womanfua = "family_f_ua.txt"
		womanotchua = "otch_f_ua.txt"

		ci = womaniua
		cf = womanfua
		co = womanotchua

		imret, famret, otchmret = imfaot(ci,cf,co)
		print(imret)
		print(otchmret)
		print(famret)	
	else:
		print("Неправильный аргумент командной строки")

	
	return 0

training()


