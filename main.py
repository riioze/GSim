#coding:utf-8
from classe import *
import random
from fonctions import *
import os
import time

os.chdir("log")
mon_fichier = open("log.txt", "w")
ninit = int(input("Combien voulez vous d'humain au départ : "))
p1 = int(input('Quel est la probabilité pour chaque géne qu\'il soit un "a" : '))
a1 = int(input("Quel est l'avantage en espérence de vie du  géne \"a\", (entre -100 pour le pire et 100 pour le meilleur) : "))
listeH = initHumain(ninit,p1,p1)
listet = trier(listeH)
listeP = tr(listeH)
fpop = open("pop.txt", "w")
fa = open("a.txt", "w")
fb = open("b.txt", "w")
faa = open("aa.txt", "w")
faap = open("aap.txt", "w")
aa = ["aa : ",len(listet[0])/len(listeH)*100,"%"]
bb = ["bb : ",len(listet[1])/len(listeH)*100,"%"]
ab = ["ab : ",len(listet[2])/len(listeH)*100,"%"]

taa = len(listet[0])

a = "0"
b = "0"

# for x in range(len(listeH)):
# 	print(listeH[x])

r = int(input("Qelle population voulez vous atteindre ? : "))

t = int(input("taux de reproduction : "))
c = 0
ti = time.time()
Année = 0
pourcentage2 = 0
while r > len(listeH):
	
	
	for x in range(int(t*len(listeH)/100)):
		reproduction(listeH,random.randint(0,len(listeH)-1),random.randint(0,len(listeH)-1))
		listeP = tr(listeH)
		# print("Année : ",Année)
		listet = trier(listeH)
		taa = len(listet[0])

		straa = str(taa/len(listeH)*100) + " %"
		p = pourcentage(listeH)
		# print("aa : " + straa + " : " + str(taa))
		a = str(len(p[0])/len(listeH)*100)+"%"
		b = str(len(p[1])/len(listeH)*100)+"%"
		# print(a)
		# print(b)
		
		# print("Fini a " + str(len(listeH)/r) + " %")
		# print("population : ", len(listeH))
		c += 1
	m = 0
	for y in range(0,len(listeH)):
		listeH[y].age += 1
		if listeH[y].gene1 == "a" and listeH[y].gene2 == "a":
			if listeH[y].age >= 80+(80*a1/100):
				listeH[y] = 0
				m += 1
		else:
			if listeH[y].age >= 80:
				listeH[y] = 0
				m += 1
	for x in range(m):
		liste.remove(0)
	straa = str(taa/len(listeH)) + " %"
	Année += 1
	w = "Année n°"+ str(Année) + " : "+ str(len(listeH)) + " humains, a : "+ a + " b : "+ b + " aa : "+ straa + " : "+ str(taa) + "\n"
	mon_fichier.write(w)

	l0_9 = ["0","1","2","3","4","5","6","7","8","9"]
	

	ca = ""
	cb = ""
	caap = ""
	la = list(str(len(p[0])/len(listeH)*100))
	for x in range(len(la)):
		if la[x] in l0_9:
			ca = ca + la[x]
		else:
			ca = ca + ","

	lb = list(str(len(p[1])/len(listeH)*100))
	for x in range(len(lb)):
		if lb[x] in l0_9:
			cb = cb + lb[x]
		else:
			cb = cb + ","

	laap = list(str(len(listet[0])/len(listeH)*100))
	for x in range(len(laap)):
		if laap[x] in l0_9:
			caap = caap + laap[x]
		else:
			caap = caap + ","

	fpop.write(str(len(listeH))+"\n")
	fa.write(str(len(p[0])) + "\n")
	fb.write(str(len(p[1])) + "\n")
	faa.write(str(taa) + "\n")
	faap.write(caap + "\n")
	pourcentage = r/len(listeH)
	if pourcentage >= pourcentage2+1:
		poucetage2 += 1
		print(pourcentage2)

print(time.time()-ti)
