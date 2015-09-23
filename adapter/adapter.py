import random
import sys

#def blender_init():
#	import 

class bouncyball:
	def __init__(self):
		self.strength_max = 10
		self.strength_min = 2
		return
	def bounce(self):
		bounce_strength = random.randrange(self.strength_min, self.strength_max)
		return bounce_strength

class howhigh(bouncyball):
	def gimmeheight(self):
		return self.bounce()

class readititome(bouncyball):
	def tellmetthings(self):
		digit = self.bounce()
		if digit > 4:
			return "it's too big"
		num_list =  ["two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
		return num_dict[digit - 2]

class leerme(bouncyball):
	def dimecosas(self):
		digit = self.bounce()
		if digit > 4:
			return "el numero es muy grande"
		num_dict = ["dos", "tres", "quatro", "cinco", "seis", "siete", "ocho", "nueve", "diez"]
		return num_dict[digit - 2]
               

