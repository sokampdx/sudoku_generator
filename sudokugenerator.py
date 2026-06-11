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
                self.grid[row + i][col + j] = nums.pop(random.randrange(len(nums)))
                
    def fill_3x3(self, row, col):
        for i in range(3):
            cur_row = row + i
            for j in range(3):
                cur_col = col + j
                while True:
                    num = random.randint(1, 9)
                    if (self.is_not_used(cur_row, cur_col, num)):
                        self.grid[cur_row][cur_col] = num
                        break
                
                
    def is_not_used(self, row, col, num):
        return self.not_in_box(row, col, num) and self.not_in_row(row, num) and self.not_in_col(col, num)
                
    def not_in_box(self, row, col, num):
        row_start = row // 3 * 3
        col_start = col // 3 * 3
        for i in range(3):
            for j in range(3):
                if (self.grid[row_start + i][col_start + j] == num):
                    return False

        return True
        
    def not_in_row(self, row, num):
        for j in range(9):
            if (self.grid[row][j] == num):
                return False
            
        return True
    
    def not_in_col(self, col, num):
        for i in range(9):
            if (self.grid[i][col] == num):
                return False
            
        return True
                    

    def generate(self):
        for i in range(0, 9, 3):
            self.fill_random_3x3(i, i)
        
        return self.grid
    
    @staticmethod
    def printGrid(grid):
        for r in grid:
            print(" ".join(map(str, r)))
    
    @staticmethod
    def emptyGrid():
        return [[0] * 9 for _ in range(9)]
    
    def reset(self):
        self.grid = [[0] * 9 for _ in range(9)]