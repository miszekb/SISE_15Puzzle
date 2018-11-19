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

def CheckNumbers(array):

	i=0
	raw_list = []

	for sub in array:
		for num in sub:
			raw_list.append(num)

	while i<len(raw_list):
		j = i+1
		while j < len(raw_list):
			if raw_list[i] == raw_list[j]:
				print("Nieprawidlowa numeracja elementow ukladanki")
				sys.exit()
			else:
				j += 1
		i += 1



