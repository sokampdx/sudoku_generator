from sudoku import Sudoku

class SudokuSolver(Sudoku):
    def solve(self):
        for i in range(9):
            for j in range(9):
                self.fill_empty(i, j)
        
        return self.grid

