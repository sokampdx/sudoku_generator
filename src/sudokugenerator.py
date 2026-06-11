import random


class SudokuGenerator:
    def __init__(self):
        self.grid = [[0] * 9 for _ in range(9)]
        
    def generate_1_to_9(self):
        return list(range(1, 10))

    def fill_random_3x3(self, row, col):
        nums = self.generate_1_to_9()
        for i in range(3):
            for j in range(3):
                while len(nums) > 0:
                    self.grid[row + i][col + i] = nums.pop(random.randrange(len(nums)))
                    

    def generate(self):
        for i in range(0, 9, 3):
            self.fill_random_3x3(i, i)
        
        return self.grid
    
    @staticmethod
    def printGrid(grid):
        for r in grid:
            print(" ".join(map(str, r)))