# Funtion for define if exist a queen in the dashboard
def verification(row, col, queens):
    if not len(queens): return False
    for queen in queens:
        if not len(queen):
            continue
        r,c = queen
        if r == row: return True # Check row
        if c == col: return True # Check column
        if (col-c) == (row-r): return True # Check left diagonal
        if (col-c) == -(row-r): return True # Check right diagonal
    return False

#Funtion for iterate in the rows solution. 
def research(n):
    numSolution = 0;
    print (n)
    solutions = None
    for row in range(1, n+1):
        # for each row, check all valid column
        solutions, numSolution = inspection(solutions, row, n, numSolution)
    print (numSolution)
    return solutions

# Funtion that evaluate the solution for iteration
def inspection(solutions, row, n, numSolution):
    print (row, n)
    #Matrix for solutions
    nSolution = []
    #Num of solution for iteration
    numSolution = 0
    for col in range(1, n+1):
        if not solutions or not len(solutions):
            nSolution.append([] + [(row, col)])
        else:
            for solution in solutions:
                if not verification(row, col, solution):
                    numSolution = numSolution + 1
                    nSolution.append(solution + [(row, col)])
    return nSolution, numSolution
print ("hola", research(8))

