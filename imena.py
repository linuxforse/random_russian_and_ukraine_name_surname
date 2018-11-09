#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

def imfaot():
	f = open("imena_m.txt","r")
	line = f.readlines()
	lenline = len(line)
	rand = random.randint(0,lenline)
	f.close()

	r = open("family_m.txt","r")
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

imret, famret = imfaot()
print(imret)
print(famret)


