import time

class HeuristicHamming:

    array = []
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
        front = [[ManhattanHeuristic(start), start]] #optional: heuristic_1
        expanded = []
        expanded_nodes=0

        while front:
            i = 0
            for j in range(1, len(front)):
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
                    newpath = [path[0] + ManhattanHeuristic(k) - ManhattanHeuristic(endnode)] + path[1:] + [k] 
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