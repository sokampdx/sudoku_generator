import random

from sudokugenerator import SudokuGenerator
from sudokusolver import SudokuSolver
from sudoku import Sudoku



if __name__ == "__main__":
    random.seed()
    
    k = 20
    sudoku = SudokuGenerator(k)
    puzzle = sudoku.generate()
    Sudoku.printGrid(puzzle)
    
    solver = SudokuSolver()
    solved = solver.solve
    Sudoku.printGrid(solved)
