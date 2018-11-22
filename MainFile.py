from TextFileHandler import *
from HeuristicHamming import *
from HeuristicManhattan import *
from BreadthFirstSearch import *
from DepthFirstSearch import *
from Controler import *

import sys

if len(sys.argv) != 6:
	print("Wprowadzono nieprawidlowa liczbe argumentow wywolania programu")
	sys.exit()

method_code = sys.argv[1]
method_parameter = sys.argv[2]
THT = TextFileHandler(sys.argv[3])
solutionFilename = sys.argv[4]
infoFilename = sys.argv[5]

THT.readFile()
print(THT.array)

solver = BreadthFirstSearch(THT.array, method_parameter, THT.col_number, THT.line_number)

CheckNumbers(THT.array)

if method_code == "bfs":
    print("Wybrano metode breadth-first search")
    CheckPermutation(method_parameter)
    
elif method_code == "dfs":
    print("Wybrano metode depth-first search")
    CheckPermutation(method_parameter)
    solver = DepthFirstSearch(THT.array, method_parameter)

elif method_code == "astr":
    print("Wybrano metode A-star")

    if method_parameter == "hamm":
        solver = HeuristicHamming(THT.array)

    elif method_parameter == "manh":
        solver = HeuristicManhattan(THT.array)

    else:
        print("Wprowadzono nieprawidlowy parametr metody")
        sys.exit()

else:
    print("Wprowadzono nieprawidlowy kod metody!")
    sys.exit()

solver.Solve()

print("Informacje na temat rozwiazania")
print("-------------------------------")
print("Dlugosc znalezionego rozwiazania: ", len(solver.solutionCode))
print("Liczba stanow odwiedzonych: ", solver.visited_states_number)
print("Liczba stanow przetworzonych: ", solver.processed_states_number)
print("Maksymalna osiagnieta glebokosc rekursji: ", solver.max_recursion_depth)
print("Czas trwania procesu obliczeniowego: ", round(solver.solving_time, 3))

THT.saveFile(solver,solutionFilename, infoFilename)
