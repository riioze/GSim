#coding:utf-8

class human:
	nh = 0

	"""docstring for human"""
	def __init__(self, sexe, num, age, gene1, gene2):
		self.age = age
		self.sexe = sexe
		self.gene1 = gene1
		self.gene2 = gene2
		human.nh+=1
		self.num = num
		self.nh = human.nh

		if sexe == 0:
			sexe = "masculin"
		else:
			sexe = "féminin"

		# print("naissance de l'humain n°{} de gene \"{}{}\" et de sexe {}".format(human.nh,gene1,gene2,sexe))
	def __str__(self):
		"""Méthode permettant d'afficher plus joliment notre objet"""
		return "L'humain n°{} a {} ans est de gene \"{}{}\" et de sexe {}".format(self.nh,self.age,self.gene1,self.gene2,self.sexe)

