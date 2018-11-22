import time

class HeuristicManhattan:

    array = []
    solving_time = 0
    solutionCode = {}
    visited_states_number = 0
    max_recursion_depth = 0
    processed_states_number = 0

    def __init__(self, array):
        self.array = array

    def Solve(self):
        print("Solving started")
        start_time = time.time()
        print("Row")
        self.solving_time = time.time() - start_time

    def calcManhattanDistance(array):
        print("Ob")
        
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
                if i < 3:                                   
                    m[i][j], m[i+1][j] = m[i+1][j], m[i][j]   #move down
                    output.append(str(m))
                    m[i][j], m[i+1][j] = m[i+1][j], m[i][j]
            if step =="L":   
                if j > 0:                                                      
                    m[i][j], m[i][j-1] = m[i][j-1], m[i][j]   #move left
                    output.append(str(m))
                    m[i][j], m[i][j-1] = m[i][j-1], m[i][j]
            if step =="R":
                if j < 3:                                   
                    m[i][j], m[i][j+1] = m[i][j+1], m[i][j]   #move right
                    output.append(str(m))
                    m[i][j], m[i][j+1] = m[i][j+1], m[i][j]