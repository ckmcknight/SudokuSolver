from SudokuSolver import solve
from samplePuzzles import *

# Sample Hard Puzzle
hard2 = '''000060840
060000005
000504170
008009200
020603050
009100700
096405000
200000080
014020000'''

# Prints the input puzzle
print(hard2.replace("0", "_").replace("",","))
print ("\n" * 3)
# Solves Puzzle
puzzle = solve(hard2)
# Prints whether or not the puzzle is solvable and then the solution
print(puzzle)


