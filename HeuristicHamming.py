import time
import pprint

class HeuristicHamming:

    array = []
    pp = pprint.PrettyPrinter(indent=3)
    solving_time = 0
    solutionCode = {}
    visited_states_number = 0
    processed_states_number = 0
    max_recursion_depth = 0

    def __init__(self, array):
        self.array = array

    def Solve(self):
        print("Solving started")
        start_time = time.time()
        front = [[self.ManhattanHeuristic(self.array), self.array]] 
        expanded = []
        expanded_nodes=0

        while front:
            i = 0
            for j in range(1, len(front)):
                sel
                if front[i][0] > front[j][0]:
                    i = j
                path = front[i]
                front = front[:i] + front[i+1:]
                endnode = path[-1]
                if endnode == end:
                    break
                if endnode in expanded: continue
                for k in moves(endnode):
                    if k in expanded: continue
                    newpath = [path[0] + self.ManhattanHeuristic(k) - ManhattanHeuristic(endnode)] + path[1:] + [k] 
                    front.append(newpath)
                    expanded.append(endnode)
            expanded_nodes += 1 
        print("Solution: ")
        print("Rozwiazywanie zakonczone!")
        self.solving_time = time.time() - start_time

    def ManhattanHeuristic(self, puzz):   
        distance = 0
        m = eval(puzz)          
        for i in range(4):
            for j in range(4):
                if m[i][j] == 0: continue
                distance += abs(i - (m[i][j]/4)) + abs(j -  (m[i][j]%4));
        return distance

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