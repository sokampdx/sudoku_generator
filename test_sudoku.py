import unittest


from sudokugenerator import Sudoku

class TestSudoku(unittest.TestCase):
    def setup_grid(self, grid, r, c):
        grid[r][c] = 1
        grid[r][c + 1] = 2
        grid[r][c + 2] = 3
        grid[r + 1][c] = 4
        grid[r + 1][c + 1] = 5
        grid[r + 1][c + 2] = 6
        grid[r + 2][c] = 7
        grid[r + 2][c + 1] = 8
        grid[r + 2][c + 2] = 9
        return grid

    def test_not_in_box_is_invalid(self):
        s = Sudoku()
        s.grid[3][4] = 1
        self.assertFalse(s.not_in_box(5, 5, 1))
        
    def test_not_in_box_is_valid(self):
        s = Sudoku()
        s.grid[3][4] = 1
        self.assertTrue(s.not_in_box(5, 5, 2))
        
    def test_not_in_row_is_invalid(self):
        s = Sudoku()
        s.grid[3][4] = 1
        self.assertFalse(s.not_in_row(3, 1))
        
    def test_not_in_row_is_valid(self):
        s = Sudoku()
        s.grid[3][4] = 1
        self.assertTrue(s.not_in_row(3, 2))
        
    def test_not_in_col_is_invalid(self):
        s = Sudoku()
        s.grid[3][4] = 1
        self.assertFalse(s.not_in_col(4, 1))
        
    def test_not_in_col_is_valid(self):
        s = Sudoku()
        s.grid[3][4] = 1
        self.assertTrue(s.not_in_col(4, 2))      
        
    def test_fill_empty_correctly(self):
        s = Sudoku()
        self.setup_grid(s.grid, 3, 3)
        s.grid[5][5] = 0
        self.assertEqual(s.grid[5][5], 0)
        s.fill_empty(5, 5)
        self.assertEqual(s.grid[5][5], 9)
        
    def test_fill_empty_not_overwrite(self):
        s = Sudoku()
        self.setup_grid(s.grid, 0, 0)
        prev = s.grid[0][0]
        s.fill_empty(0, 0)
        self.assertEqual(s.grid[0][0], prev)
        
    def test_fill_empty_overwrite(self):
        s = Sudoku()
        self.setup_grid(s.grid, 0, 0)
        self.setup_grid(s.grid, 3, 3)
        self.setup_grid(s.grid, 6, 6)
        prev = s.grid[3][0]
        self.assertEqual(prev, 0)
        s.fill_empty(3, 0)
        self.assertNotEqual(s.grid[3][0], prev)