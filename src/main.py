
import random


def sudoku_generator(empty):
    pass

if __name__ == "__main__":
    random.seed()
    
    k = 20
    puzzle = sudoku_generator(k)
    
    for r in puzzle:
        print(" ".join(map(str, r)))
