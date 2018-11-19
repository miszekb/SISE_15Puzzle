import time
import pprint
import ast

class BreadthFirstSearch:
    pp = pprint.PrettyPrinter(indent=3)
    col_size = 0
    ver_size = 0
    end = str([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12],[13, 14, 15, 0]])

    array = []
    order = {}
    solving_time = 0
    solutionCode = {}
    visited_states_number = 0
    processed_states_number = 0
    max_recursion_depth = 0

    def __init__(self, array, order, col_size, ver_size):
        self.col_size = col_size
        self.ver_size = ver_size
        self.array = array
        self.order = list(order)

    def moves(self, mat):
        output = []
        m = eval(mat)   
        i = 0
        while 0 not in m[i]: i += 1
        j = m[i].index(0); #blank space (zero)

        if i > 0:                                   
            m[i][j], m[i-1][j] = m[i-1][j], m[i][j];  #move up
            output.append(str(m))
            m[i][j], m[i-1][j] = m[i-1][j], m[i][j]; 
              
        if i < 3:                                   
            m[i][j], m[i+1][j] = m[i+1][j], m[i][j]   #move down
            output.append(str(m))
            m[i][j], m[i+1][j] = m[i+1][j], m[i][j]

        if j > 0:                                                      
            m[i][j], m[i][j-1] = m[i][j-1], m[i][j]   #move left
            output.append(str(m))
            m[i][j], m[i][j-1] = m[i][j-1], m[i][j]

        if j < 3:                                   
            m[i][j], m[i][j+1] = m[i][j+1], m[i][j]   #move right
            output.append(str(m))
            m[i][j], m[i][j+1] = m[i][j+1], m[i][j]

        return output

    def Solve(self):
        print("Solving started")
        start_time = time.time()
        front = [[str(self.array)]]
        expanded = []
        expanded_nodes=0

        while front:
            i = 0
            for j in range(1, len(front)):    #minimum
                if len(front[i]) > len(front[j]):
                    i = j
            path = front[i]         
            front = front[:i] + front[i+1:]
            endnode = path[-1]
            if endnode in expanded: continue
            for k in self.moves(endnode):
                if k in expanded: continue
                print("szukam")
                front.append(path + [k])
            expanded.append(endnode)
            expanded_nodes += 1
            if endnode == self.end: break
        self.solving_time = time.time() - start_time
        print("Expanded nodes:",expanded_nodes)
        print("Solution:")
        self.pp.pprint(path[0])
        print(self.DetermineSteps(path))
        print("Rozwiazywanie zakonczone!")

    def DetermineSteps(self, solution_array):

        steps_array = []
        diff_array = []
        sol_array1 = eval(solution_array)

        for i in range(0, len(solution_array) - 1):
            print("l")
            sol_array1.append(ast.literal_eval(solution_array[i]))
            for j in range(0, len(solution_array[0]) - 1):
                sol_array2.append(ast.literal_eval(sol_array1))
                for k in range(0, len(solution_array[0][0]) - 1):
                    sol_array3.append(ast.literal_eval(sol_array2))
                    if sol_array3[i][j][k] == "0":
                        print("k")
                        diff_array.append([j,k])

        for i in range(1, len(diff_array) - 1):
            if diff_array[i][0] > diff_array[i-1][0]:
                steps_array.append("D")
            if diff_array[i][0] < diff_array[i-1][0]:
                steps_array.append("U")
            if diff_array[i][1] > diff_array[i-1][1]:
                steps_array.append("R")    
            if diff_array[i][1] < diff_array[i-1][1]:
                steps_array.append("L")
        return steps_array
