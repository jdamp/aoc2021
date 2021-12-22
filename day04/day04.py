import re

import numpy as np

class Board:
    def __init__(self, size, data) -> None:
        self.size = size
        self.data = data
        self.marked = np.zeros((self.size, self.size), dtype=bool)
        self.last_number = None

    def mark(self, number: int):
        self.last_number = number
        self.marked |= (self.data == number)

    def check(self):
        row_check = (self.marked.sum(axis=0) == self.size).any()
        col_check = (self.marked.sum(axis=1) == self.size).any()
        return row_check or col_check

    def score(self):
        unmarked = self.data[~self.marked]
        return unmarked.sum()*self.last_number

    def __repr__(self):
        return f"{self.data.__repr__()}\n"

    def __eq__(self, other: object) -> bool:
        return self.data == other.data and self.marked == other.marked


if __name__ == "__main__":
    boards = []
    with open("input.txt", 'r') as f:
        lines = f.readlines()
        size = 5
        # First row is the header
        numbers = [int(n) for n in lines[0].split(",")]        
        # A board has six lines: one empty line, and five with contents
        for iboard in range((len(lines)-1)//6):
            lower = 2 + (1 + size) * iboard
            upper = lower + size
            data = np.array([re.split(" +", l.strip()) for l in lines[lower:upper]], 
            dtype=int)
            boards.append(Board(size, data))
    
    winning_board = None
    for number in numbers:
        if winning_board is not None:
            break
        for board in boards:
            board.mark(number)
            if board.check():
                winning_board = board
                
    print(f"Part 1: {winning_board.score()}")

    boards_won = []    
    for number in numbers:
        for iboard, board in list(enumerate(boards))[::-1]:
            board.mark(number)
            if board.check():                
                boards_won.append(boards.pop(iboard))
                  
    print(f"Part 2: {boards_won[-1].score()}")