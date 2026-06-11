import unittest


from src.sudokugenerator import SudokuGenerator

class TestSudokuGenerator(unittest.TestCase):
    
    def test_fill_random_3x3(self):
        s = SudokuGenerator()
        s.fill_random_3x3(0, 0)
        self.assertNotEqual(s.grid[0][0], 0)
        self.assertNotEqual(s.grid[2][2], 0)
        self.assertEqual(s.grid[3][0], 0)
        self.assertEqual(s.grid[0][3], 0)
        
        
if __name__ == "__main__":
    unittest.main()