import time
import pprint
import ast
import sys

class BreadthFirstSearch:
    pp = pprint.PrettyPrinter(indent=3)
    col_size = 0
    ver_size = 0
    end = []

    array = []
    order = {}
    solving_time = 0
    solutionCode = []
    visited_states_number = 0
    processed_states_number = 0
    max_recursion_depth = 0

    def __init__(self, array, order, col_size, ver_size, pattern):
        self.col_size = col_size
        self.ver_size = ver_size
        self.array = array
        self.order = list(order)
        self.end = str(pattern)

    def moves(self, mat):
        output = []
        m = eval(mat)   
        i = 0
        while 0 not in m[i]: i += 1
        j = m[i].index(0); #blank space (zero)

        for step in self.order:
            if step == "U":
                if i > 0:                                   
                    m[i][j], m[i-1][j] = m[i-1][j], m[i][j];  #move up
                    output.append(str(m))
                    m[i][j], m[i-1][j] = m[i-1][j], m[i][j]; 
            if step == "D":          
                if i < self.ver_size-1:                                   
                    m[i][j], m[i+1][j] = m[i+1][j], m[i][j]   #move down
                    output.append(str(m))
                    m[i][j], m[i+1][j] = m[i+1][j], m[i][j]
            if step =="L":   
                if j > 0:                                                      
                    m[i][j], m[i][j-1] = m[i][j-1], m[i][j]   #move left
                    output.append(str(m))
                    m[i][j], m[i][j-1] = m[i][j-1], m[i][j]
            if step =="R":
                if j < self.col_size-1:                                   
                    m[i][j], m[i][j+1] = m[i][j+1], m[i][j]   #move right
                    output.append(str(m))
                    m[i][j], m[i][j+1] = m[i][j+1], m[i][j]

        return output

    def Solve(self):
        print("Solving started")
        start_time = time.time()
        front = [[str(self.array)]]
        expanded = []

        while front: #jeśli nie jest puste
            self.pp.pprint((front[0]))
            i = 0
            path = front[0]
            front = front[i+1:] #wszystkie oprocz front[i]
            endnode = path[-1] #ostatni element
            if endnode in expanded: continue
            for k in self.moves(endnode):
                #self.pp.pprint(self.moves(endnode))
                #self.pp.pprint(endnode)
                if k in expanded: continue
                front.append(path + [k])
            expanded.append(endnode)
            #print(i)      
            self.processed_states_number += 1
            if endnode == self.end: break # jeśli się pokrywa to koniec
        self.solving_time = time.time() - start_time
        print("Expanded nodes:",self.processed_states_number)
        self.max_recursion_depth = len(path) - 1
        print("Solution:")
        print(self.DetermineSteps(path))
        print("Rozwiazywanie zakonczone!")

    def DetermineSteps(self, solution_array):
        steps_array = []

        for k in range(0, len(solution_array)):
            m = eval(solution_array[k])
            print(m)
            i = 0
            while 0 not in m[i]: i += 1
            j = m[i].index(0);
            steps_array.append([i,j])
        for k in range(1, len(steps_array)):
            if steps_array[k][0] > steps_array[k-1][0]: self.solutionCode.append("U")
            if steps_array[k][0] < steps_array[k-1][0]: self.solutionCode.append("D")
            if steps_array[k][1] > steps_array[k-1][1]: self.solutionCode.append("L")
            if steps_array[k][1] < steps_array[k-1][1]: self.solutionCode.append("R")
        print(''.join(self.solutionCode))

