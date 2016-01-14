# Implementation for a puzzle object
#   Puzzle's know the puzzle
#   Whether or not its solved
#   And how to represent it as a string
class SudokuPuzzle():

    def __init__(self, puzzleString):
        self.originalPuzzleString = puzzleString
        self.grid = self.readPuzzle(puzzleString)
        self.isSolved = False

    # Takes in a puzzle string and returns a puzzle with a list of all possible options for each
    def readPuzzle(self, puzzle_txt):
        pzzl = puzzle_txt.split()
        pzzl = [[range(1,len(row)+1) if char == "0" else [int(char)] for char in row] for row in pzzl]
        return pzzl

    # Prints out a string representation of the puzzle
    def __str__(self):
        out = "Puzzle is solved: " + str(self.isSolved) + "\n"
        for row in self.grid:
            for col in row:
                out += str(col)
            out += "\n"
        return out

