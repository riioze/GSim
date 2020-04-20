#coding:utf-8
from classe import *
import random
from time import *
import os
liste = []
def initHumain(n,pga1,pga2):
	t = time()
	for x in range(n):
		g = random.randint(0,100)
		if g in range(pga1):
			g1 = "a"
		else:
			g1 = "b"
		g = random.randint(0,100)
		if g in range(pga2):
			g2 = "a"
		else:
			g2 = "b"
		

		liste.append(human(random.randint(0,1),x,0,g1,g2))
		a = float(x)/float(n)*100
		# print(a,"%")
		# os.system("cls")
	t2 = time()-t
	print(t2)
	return liste

def trier(liste):
	aa = []
	ab = []
	bb = []
	for x in range(len(liste)):
		if liste[x].gene1 == "a" and liste[x].gene2 == "a":
			aa.append(liste[x])
		if liste[x].gene1 == "b" and liste[x].gene2 == "b":
			bb.append(liste[x])
		if liste[x].gene1 == "a" and liste[x].gene2 == "b":
			ab.append(liste[x])
		if liste[x].gene1 == "b" and liste[x].gene2 == "a":
			ab.append(liste[x])
	l = []
	l.append(aa)
	l.append(bb)
	l.append(ab)
	return l

def reproduction(liste,h1,h2):
	g1h1 = liste[h1].gene1
	g2h1 = liste[h1].gene2
	g1h2 = liste[h2].gene1
	g2h2 = liste[h2].gene2
	g1 = random.randint(0,1)
	g2 = random.randint(0,1)
	if g1 == 0:
		g1 = g1h1
	else:
		g1 = g1h2
	if g2 == 0:
		g2 = g2h1
	else:
		g2 = g2h2
	x = len(liste)
	liste.append(human(random.randint(0,1),x,0,g1,g2))
	# os.system("cls")
	return liste

def pourcentage(liste):
	a = []
	b = []
	for x in range(len(liste)):
		if liste[x].gene1 == "a" or liste[x].gene2 == "a":
			a.append(liste[x])
		if liste[x].gene1 == "b" or liste[x].gene2 == "b":
			b.append(liste[x])

	l = []
	l.append(a)
	l.append(b)

	return l

def tr(liste):
	a = []
	na = []
	b =[]
	nb = []
	l = []
	for x in range(len(liste)):
		if liste[x].gene1 == "a" or liste[x].gene2 == "a":
			a.append(liste[x])
		else:
			na.append(liste[x])
		if liste[x].gene1 == "b" or liste[x].gene2 == "b":
			b.append(liste[x])
		else:
			nb.append(liste[x])

	l.append(a)
	l.append(na)
	l.append(b)
	l.append(nb)
	return l
