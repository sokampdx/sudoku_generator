import unittest


from sudokugenerator import SudokuGenerator

class TestSudokuGenerator(unittest.TestCase):
    
    def test_fill_random_3x3_is_valid(self):
        s = SudokuGenerator()
        s.fill_random_3x3(0, 0)
        self.assertNotEqual(s.grid[0][0], 0)
        self.assertNotEqual(s.grid[1][2], 0)
        self.assertEqual(s.grid[3][0], 0)
        self.assertEqual(s.grid[2][4], 0)
        self.assertEqual(s.grid[4][4], 0)
        self.assertEqual(s.grid[6][8], 0)
        self.assertEqual(s.grid[8][5], 0)
        
        s.fill_random_3x3(3, 3)
        self.assertEqual(s.grid[2][4], 0)
        self.assertNotEqual(s.grid[4][4], 0)
        self.assertEqual(s.grid[6][8], 0)
        self.assertEqual(s.grid[8][5], 0)
        
        s.fill_random_3x3(6, 6)
        self.assertNotEqual(s.grid[6][8], 0)
        self.assertEqual(s.grid[8][5], 0)
        
    def test_not_in_box_is_invalid(self):
        s = SudokuGenerator()
        s.grid[3][4] = 1
        self.assertFalse(s.not_in_box(5, 5, 1))
        
    def test_not_in_box_is_valid(self):
        s = SudokuGenerator()
        s.grid[3][4] = 1
        self.assertTrue(s.not_in_box(5, 5, 2))
        
    def test_not_in_row_is_invalid(self):
        s = SudokuGenerator()
        s.grid[3][4] = 1
        self.assertFalse(s.not_in_row(3, 1))
        
    def test_not_in_row_is_valid(self):
        s = SudokuGenerator()
        s.grid[3][4] = 1
        self.assertTrue(s.not_in_row(3, 2))
        
    def test_not_in_col_is_invalid(self):
        s = SudokuGenerator()
        s.grid[3][4] = 1
        self.assertFalse(s.not_in_col(4, 1))
        
    def test_not_in_col_is_valid(self):
        s = SudokuGenerator()
        s.grid[3][4] = 1
        self.assertTrue(s.not_in_col(4, 2))      
        
    def test_fill_empty(self):
        s = SudokuGenerator()
        s.grid[3][3] = 1
        s.grid[3][4] = 2
        s.grid[3][5] = 3
        s.grid[4][3] = 4
        s.grid[4][4] = 5
        s.grid[4][5] = 6
        s.grid[5][3] = 7
        s.grid[5][4] = 8
        self.assertEqual(s.grid[5][5], 0)
        s.fill_empty(5, 5)
        self.assertEqual(s.grid[5][5], 9)
        
    def test_fill_empty_not_overwrite(self):
        s = SudokuGenerator()
        s.fill_random_3x3(0, 0)
        prev = s.grid[0][0]
        s.fill_empty(0, 0)
        self.assertEqual(s.grid[0][0], prev)
        
    def test_fill_empty_overwrite(self):
        s = SudokuGenerator()
        s.fill_random_3x3(0, 0)
        s.fill_random_3x3(3, 3)
        s.fill_random_3x3(6, 6)
        prev = s.grid[3][0]
        self.assertEqual(prev, 0)
        s.fill_empty(3, 0)
        self.assertNotEqual(s.grid[3][0], prev)
        
    def test_generate_has_no_zero(self):
        s = SudokuGenerator()
        s.generate()
        SudokuGenerator.printGrid(s.grid)
        for i in range(9):
            for j in range(9):
                self.assertNotEqual(s.grid[i][j], 0)        
    
if __name__ == "__main__":
    unittest.main()