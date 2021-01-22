import datetime

#import library for conection db
from sqlalchemy import create_engine

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
    solutions = None
    for row in range(1, n+1):
        # for each row, check all valid column
        solutions, numSolution = inspection(solutions, row, n, numSolution)
    return solutions, numSolution

# Funtion that evaluate the solution for iteration
def inspection(solutions, row, n, numSolution):
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


#Funtion for database conect
def dbconect(userN, pw, host, port,tName):
    dbString = "postgresql://"+userN+":"+pw+"@"+host+":"+port;
    db = create_engine(dbString)
    db.execute("DROP TABLE IF EXISTS " + tName )
    db.execute("DROP SCHEMA IF EXISTS "+ tName)
    db.execute("CREATE TABLE IF NOT EXISTS "+ tName  +"(queen text,iter text,dx text,dy text)")
    return db

#Funtion for add data in table 
def dbinsert(db,tName, queen, itera, dx, dy):
    db.execute("INSERT INTO "+ tName +" (queen, iter, dx, dy) VALUES ("+queen+", "+itera+", "+dx+","+dy+")")
    #reader = db.execute("SELECT * FROM "+ tName)
    #for r in reader:
    #    print(r)


tName = "queenR"
value = raw_input("N :")
queen = int(value)
current_time = datetime.datetime.now() 
print(current_time)
db = dbconect("postgres","mysecretpassword","localhost","5432", tName)
solution, numSolution = research(queen)
a = solution
iTb = 0 
for row in a:
    iTb = iTb +1
    for elem in row: 
        dbinsert(db,tName,str(queen),str(iTb),str(elem[0]),str(elem[1]))
current_time = datetime.datetime.now()
print(current_time)
print("Soluciones almacenadas: " + str(numSolution))
