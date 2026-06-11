class Sudoku:
    def __init__(self):
        self.grid = [[0] * 9 for _ in range(9)]

    @classmethod
    def generate_1_to_9(self):
        return list(range(1, 10))
    
    def fill_empty(self, row, col):
        if row == 9:
            return True
        
        if col == 9:
            return self.fill_empty(row + 1, 0)
        
        if self.grid[row][col] != 0:
            return self.fill_empty(row, col + 1)
        
        for num in range(1, 10):
            if self.is_not_used(row, col, num):
                self.grid[row][col] = num
                if self.fill_empty(row, col + 1):
                    return True
                self.grid[row][col] = 0
                
        return False
    
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
    
    @staticmethod
    def printGrid(grid):
        for r in grid:
            print(" ".join(map(str, r)))
    
    @staticmethod
    def emptyGrid():
        return [[0] * 9 for _ in range(9)]
    
    def reset(self):
        self.grid = [[0] * 9 for _ in range(9)]