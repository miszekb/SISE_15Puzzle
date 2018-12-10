import sys

class TextFileHandler:

    filename = ""
    col_number = 0
    line_number = 0
    array = []

    def __init__(self, filename):
        self.filename = filename

    def readFile(self):
        self.file_object = open(self.filename, "r")

        with open(self.filename) as f:

            self.line_number, self.col_number = [int(x) for x in next(f).split()]

            for line in f:  
                self.array.append([int(x) for x in line.split()])

        if (self.col_number * self.line_number) != (len(self.array)*len(self.array[0])):
            print("Blad formatu danych wejsciowych")
            sys.exit()

        for line in self.array:
            if len(line) != self.col_number:
                print("Blad formatu danych wejsciowych")
                sys.exit()
  
    def saveFile(self, solver_obj, solution_filename, info_filename):
        infoFile = open(info_filename, "w")
        solutionFile = open(solution_filename, "w")
           
        infoFile.write(str(len(solver_obj.solutionCode)) + "\n")
        infoFile.write(str(solver_obj.visited_states_number) + "\n")
        infoFile.write(str(solver_obj.processed_states_number) + "\n")
        infoFile.write(str(solver_obj.max_recursion_depth) + "\n")
        infoFile.write(str(round(solver_obj.solving_time, 3)))
        infoFile.close()

        string_buf = "".join(solver_obj.solutionCode)
        #solutionFile.write(str(len(solver_obj.solutionCode)) + "\n")
        solutionFile.write(string_buf)
        solutionFile.close()




                    


