import time

class BreadthFirstSearch:

    array = []
    order = {}
    solving_time = 0
    solutionCode = {}
    visited_states_number = 0
    processed_states_number = 0
    max_recursion_depth = 0

    def __init__(self, array, order):
        self.array = array
        self.order = list(order)

    def Solve(self):
    	print("Solving started")
    	start_time = time.time()

    	print("Rozwiazywanie zakonczone!")
    	self.solving_time = time.time() - start_time
