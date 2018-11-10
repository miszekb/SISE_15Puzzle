import sys

def CheckPermutation(string):

	if_R = 0
	if_L = 0
	if_U = 0
	if_D = 0
	
	characters = list(string)

	for char in characters:

		if char == "R":
			if_R = 1
		elif char == "L":
			if_L = 1
		elif char == "U":
			if_U = 1
		elif char == "D":
			if_D = 1

	if if_R != 1 or if_L != 1 or if_U != 1 or if_D!= 1:
		print("Wprowadzono nieprawidlowy parametr metody!")
		sys.exit()






