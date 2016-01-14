# The isSolved Function checks to see if a puzzle is solved
def isSolved (grid):
    if (isLenOne(grid)):
        return squareChecker(grid) and columnChecker(grid) and rowChecker(grid)
    else:
        return False

#Checks to see if the group has the correct numbers.
def checkComplete(group):
    alreadyin=[]
    for x in group:
        if x in alreadyin:
            return False
        alreadyin+=[x]
    return True

#Checks to see if the squares are completed
def squareChecker(grid):
    change=True
    for boxRow in range(3):
        for boxCol in range(3):
            square=[]
            for x in range(3):
                for y in range(3):
                    square+=[grid[boxRow*3+x][boxCol*3+y]]
            change=change and checkComplete(square)
    return change

# Checks to see if the columns are complete
def columnChecker(grid):
    change=True
    for column in range(9):
        columny=[]
        for row in range(9):
            columny+=[grid[row][column]]
        change= change and checkComplete(columny)
    return change

#checks to see if the rows are complete
def rowChecker(grid):
    change=True
    for row in range(9):
        rowy=[]
        for box in range(9):
            rowy+=[grid[row][box]]
        change=change and checkComplete(rowy)
    return change

# Checks to see if each puzzle only has one option for each box
def isLenOne(grid):
    for row in grid:
        for box in row:
            if len(box) !=1:
                return False
    return True
