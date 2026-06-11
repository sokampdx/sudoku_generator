import random

from sudoku import Sudoku


class SudokuGenerator(Sudoku):
    def __init__(self, k = 0):
        super().__init__()
        self.num_empty = k

    def fill_random_3x3(self, row, col):
        nums = self.generate_1_to_9()
        for i in range(3):
            for j in range(3):
                self.grid[row + i][col + j] = nums.pop(random.randrange(len(nums)))
                                 
    def create_empty_cell(self, num):
        for _ in range(num):
            i = random.randint(0,8)
            j = random.randint(0,8)
            while self.grid[i][j] == 0:
                i = random.randint(0,8)
                j = random.randint(0,8)
            self.grid[i][j] = 0
        
    def generate(self):
        for i in range(0, 9, 3):
            self.fill_random_3x3(i, i)
            
        for i in range(9):
            for j in range(9):
                self.fill_empty(i, j)
        
        self.create_empty_cell(self.num_empty)
        
        return self.grid