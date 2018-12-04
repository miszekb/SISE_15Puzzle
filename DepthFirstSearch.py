import time

class DepthFirstSearch:
    
    array = []
    order = {}
    solving_time = 0
    solutionCode = {}
    visited_states_number = 0
    processed_states_number = 0
    max_recursion_depth = 0
    end = []

    def __init__(self, array, order, pattern):
        self.end = str(pattern)
        self.array = array
        self.order = list(order)

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
            if step == "L":   
                if j > 0:                                                      
                    m[i][j], m[i][j-1] = m[i][j-1], m[i][j]   #move left
                    output.append(str(m))
                    m[i][j], m[i][j-1] = m[i][j-1], m[i][j]
            if step == "R":
                if j < self.col_size-1:                                   
                    m[i][j], m[i][j+1] = m[i][j+1], m[i][j]   #move right
                    output.append(str(m))
                    m[i][j], m[i][j+1] = m[i][j+1], m[i][j]
        return output

    def Solve(self):
        print("Solving started")
        start_time = time.time()

        while self.array:
            branch = self.array
            branch.append(self.moves(self.array))
            if self.max_recursion_depth == 21: break
            for i in range(0, 21):
                branch.append(self.moves(branch))
            self.max_recursion_depth += 1

        print("Rozwiazywanie zakonczone!")
        self.solving_time = time.time() - start_time

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

