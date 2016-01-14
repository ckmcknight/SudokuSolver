from EasySudokuSolver import solveEasy
from IsSudokuSolved import isSolved
from PuzzleReader import SudokuPuzzle
from copy import deepcopy

def solve(puzzleStr):
    puzzle = SudokuPuzzle(puzzleStr)
    puzzle.grid = solveHard(puzzle.grid)
    puzzle.isSolved = isSolved(puzzle.grid)
    return puzzle

def impossiblePuzzle(grid):
    for row in grid:
        for box in row:
            if len(box) == 0:
                return True
    return False

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

print(solve(hard2))
