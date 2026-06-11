import random

from src.sudokugenerator import SudokuGenerator


if __name__ == "__main__":
    random.seed()
    
    k = 20
    sudoku = SudokuGenerator()
    
    SudokuGenerator.printGrid(sudoku.generate())
