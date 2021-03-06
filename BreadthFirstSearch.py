import time
import pprint
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
        self.end = (pattern)
        
    def Solve(self):
        print("Solving started")
        start_time = time.time()
        expanded = []
        path = self.bfs((self.array), self.end, self.num_moves(self.ver_size, self.col_size))

        self.solving_time = time.time() - start_time
        print("Expanded nodes:", len(expanded))
        self.max_recursion_depth = len(path) - 1
        print("Solution:")
        print(self.DetermineSteps(path))
        print("Rozwiazywanie zakonczone!")

    def DetermineSteps(self, solution_array):
        steps_array = []

        for k in range(0, len(solution_array)):
            m =solution_array[k]
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

    def bfs(self, puzzle, goal, get_moves):
        queue = []
        queue.append([puzzle])
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == goal:
                return path
            else:
                self.visited_states_number += 1

            for adjacent in (get_moves(node)):
                if adjacent not in path:
                    new_path = list(path)
                    new_path.append(adjacent)
                    queue.append(new_path)
                    if self.max_recursion_depth < len(path) - 1:
                        self.max_recursion_depth = len(path) - 1

    def num_moves(self, rows, cols):
        def get_moves(subject):
            moves = []

            zrow, zcol = next((r, c)
                for r, l in enumerate(subject)
                    for c, v in enumerate(l) if v == 0)

            def swap(row, col):
                import copy
                s = copy.deepcopy(subject)
                s[zrow][zcol], s[row][col] = s[row][col], s[zrow][zcol]
                return s

            for step in self.order:
                if step == "R":                     
                    if zcol > 0:
                        print("1")
                        moves.append(swap(zrow, zcol - 1))
                if step == "U":        
                    if zrow < rows - 1:
                        print("2")
                        moves.append(swap(zrow + 1, zcol))
                if step == "D":  
                    if zrow > 0:
                        print("3")
                        moves.append(swap(zrow - 1, zcol))
                if step == "L":        
                    if zcol < cols - 1:
                        print("4")
                        moves.append(swap(zrow, zcol + 1)) 
            return moves
        return get_moves