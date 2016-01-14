from PuzzleReader import SudokuPuzzle
from IsSudokuSolved import isSolved
from copy import deepcopy

#Solves a puzzle supplied in the correct format and returns a puzzle object
def solve(puzzleStr):
    puzzle = SudokuPuzzle(puzzleStr)
    puzzle.grid = solveHard(puzzle.grid)
    puzzle.isSolved = isSolved(puzzle.grid)
    return puzzle

# Solves all Sudoku puzzles
def solveHard(grid):
    solveEasy(grid)
    if isSolved(grid) or impossiblePuzzle(grid):
        return grid
    for row in range(len(grid)):
        for column in range(len(grid)):
            if len(grid[row][column]) != 1:
                for number in grid[row][column]:
                    copyGrid = deepcopy(grid)
                    copyGrid[row][column] = [number]
                    copyGrid = solveHard(copyGrid)
                    if isSolved(copyGrid):
                        return copyGrid
    return grid

# Takes in a puzzle object and solves as much as it can without guessing
# This will solves all puzzles of Easy difficulty
def solveEasy(grid):
    change=True
    while change:
        change=False
        change=rowMaker(grid) or columnMaker(grid) or squareMaker(grid)

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

# Determines if a puzzle is impossible to solve
def impossiblePuzzle(grid):
    for row in grid:
        for box in row:
            if len(box) == 0:
                return True
    return False
