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
               
    def test_generate_has_no_zero(self):
        s = SudokuGenerator()
        s.generate()
        SudokuGenerator.printGrid(s.grid)
        for i in range(9):
            for j in range(9):
                self.assertNotEqual(s.grid[i][j], 0)      
                
    def test_create_empty_cell_has_correct_num_of_0(self):
        s = SudokuGenerator()
        s.grid = [
            [7, 1, 8, 3, 2, 5, 4, 9, 6],
            [6, 5, 3, 4, 9, 1, 7, 2, 8],
            [4, 2, 9, 6, 7, 8, 1, 3, 5],
            [1, 3, 5, 7, 6, 4, 9, 8, 2],
            [8, 4, 6, 2, 1, 9, 3, 5, 7],
            [2, 9, 7, 5, 8, 3, 6, 1, 4],
            [3, 8, 2, 1, 4, 6, 5, 7, 9],
            [9, 6, 1, 8, 5, 7, 2, 4, 3],
            [5, 7, 4, 9, 3, 2, 8, 6, 1]          
        ]
        for i in range(9):
            for j in range(9):
                self.assertNotEqual(s.grid[i][j], 0)      
                
        num_empty = 10
        s.create_empty_cell(num_empty)

        count = 0
        for i in range(9):
            for j in range(9):
                if s.grid[i][j] == 0:
                    count = count + 1
        self.assertEqual(count, num_empty)    
                  
    
if __name__ == "__main__":
    unittest.main()