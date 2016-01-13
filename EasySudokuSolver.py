from PuzzleReader import SudokuPuzzle
from IsSudokuSolved import isSolved

def solve(puzzleStr):
    puzzle = SudokuPuzzle(puzzleStr)
    solveEasy(puzzle)
    print("Puzzle is solved: " + str(puzzle.isSolved))
    print(str(puzzle))


# Takes in a puzzle object and solves as much as it can without guessing
def solveEasy(puzzle):
    change=True
    grid = puzzle.grid
    while change:
        change=False
        change=rowMaker(grid) or columnMaker(grid) or squareMaker(grid)
    puzzle.isSolved = isSolved(puzzle)

# Takes in a Row, Column, or box as a 1D list and removes possiblites based on
# Completed Squares
def rewritePuzzle(changeGroup):
    change = False
    takenSpots = []
    for x in changeGroup:
        if len(x) == 1:
            takenSpots += [x[0]]
    for y in changeGroup:
        if len(y) > 1:
            for z in takenSpots:
                if z in y:
                    change=True
                    y.remove(z)
    return change

# Figures out which each row is and sends it to rewrite puzzle to be analyzed
def rowMaker(grid):
    change = False
    for row in grid:
        change = change or rewritePuzzle(row)
    return change

# Figures out which each row is and sends it to rewrite puzzle to be analyzed
def columnMaker(grid):
    change = False
    for x in range(9):
        column = []
        for y in range(9):
            column.append(grid[y][x])
        change = change or rewritePuzzle(column)
    return change

# Figures out which each row is and sends it to rewrite puzzle to be analyzed
def squareMaker(grid):
    change = False
    for boxRow in range(3):
        for boxCol in range(3):
            square = []
            for x in range(3):
                for y in range(3):
                    square.append(grid[boxRow*3+x][boxCol*3+y])
            change = change or rewritePuzzle(square)
    return change

hard2 = '''000060840
060000005
000504170
008009200
020603050
009100700
096405000
200000080
014020000'''

easy = '''003020600
900305001
001806400
008102900
700000008
006708200
002609500
800203009
005010300'''

easy2= '''600000058
450801000
800070130
204057900
700206003
006480502
061040007
000708016
970000005'''

print(solve(easy2))

