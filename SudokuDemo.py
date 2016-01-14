from SudokuSolver import solve

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
print("This is the original puzzle of Hard difficulty:\n")
print(hard2.replace("0", "_").replace("",","))
print ("\n" * 2)
# Solves Puzzle
puzzle = solve(hard2)
# Prints whether or not the puzzle is solvable and then the solution
print("This is the solution:\n")
print(puzzle)


