import time
import pprint

class HeuristicHamming:

    array = []
    pp = pprint.PrettyPrinter(indent=3)
    solving_time = 0
    solutionCode = []
    visited_states_number = 0
    processed_states_number = 0
    max_recursion_depth = 0
    end = []

    def __init__(self, array, pattern):
        self.array = str(array)
        self.end = str(pattern)

    def Solve(self):
        print("Solving started")
        start_time = time.time()
        front = [[self.HammingHeuristic(self.array), self.array]] 
        expanded = []
        expanded_nodes=0
        #self.pp.pprint(front)
        while front:
            i = 0
            for j in range(1, len(front)):
	            if front[i][0] > front[j][0]:
	                i = j
            path = front[i]
            front = front[:i] + front[i+1:]
            endnode = path[-1]
            if endnode == self.end:
                break
            if endnode in expanded: continue
            for k in self.moves(endnode):
                if k in expanded: continue
                newpath = [path[0] + self.HammingHeuristic(k) - self.HammingHeuristic(endnode)] + path[1:] + [k] 
                front.append(newpath)
                expanded.append(endnode)
            self.processed_states_number += 1
        print("Solution: ")
        print(self.DetermineSteps(path[1:]))
        print("Rozwiazywanie zakonczone!")
        self.solving_time = time.time() - start_time

    def HammingHeuristic(self, puzz):   
	    misplaced = 0
	    compare = 1
	    m = eval(puzz)
	    for i in range(4):
	        for j in range(4):
	            if m[i][j] != compare:
	                misplaced += 1
	            compare += 1
	    return misplaced

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