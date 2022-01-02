import numpy as np
from typing import Generator
from collections import Counter

def parse_input(filename: str) -> Generator[tuple[list[str], list[str]], None, None]:
    with open(filename, 'r') as f:
        for line in f.readlines():
            # get rid of spaces around the splitting character
            line = line.replace(" | ", "|")
            pattern, output = line.strip().split("|")
            patterns = ["".join(sorted(p)) for p in pattern.split(" ")]
            outputs = ["".join(sorted(o)) for o in output.split(" ")]
            yield patterns, outputs

def pattern_to_matrix(codes: list[str]) -> np.array:
    # transforms pattern to 10x7 matrix indicating which letter occurs in which digit
    out = np.zeros(shape=(10, 7))
    for row, code in enumerate(codes):
        for i in range(ord('a'), ord('g')+1):
            if chr(i) in code:
                out[row, i-ord('a')] = 1
    return out


def count_matrix(M: np.ndarray) -> np.ndarray:
    """
    Return permutation of rows according to counts of letters in all 10 digits
    """
    letter_counts = M.sum(axis=0)
    A = np.tile(np.arange(0, 7), 10).reshape(10, 7)
    M_count =  letter_counts[A]*M
    return M_count.sum(axis=1).argsort()


# Original Mapping (a,b,c,d,e,f,g)->(0,1,2,3,4,5,6,7,8,9)
M = np.array([
    [1,1,1,0,1,1,1], # 0
    [0,0,1,0,0,1,0], # 1
    [1,0,1,1,1,0,1], # 2
    [1,0,1,1,0,1,1], # 3
    [0,1,1,1,0,1,0], # 4
    [1,1,0,1,0,1,1], # 5
    [1,1,0,1,1,1,1], # 6
    [1,0,1,0,0,1,0], # 7
    [1,1,1,1,1,1,1], # 8
    [1,1,1,1,0,1,1], # 9
])

if __name__ == "__main__":
    numbers = count_matrix(M)
    counter = Counter() # part a
    digit_numbers = [] # part b
    for pattern, output in parse_input("input.txt"):
        incount = count_matrix(pattern_to_matrix(pattern))
        pattern_map = dict(zip(np.array(pattern)[incount], numbers))
        decoded = [pattern_map[o] for o in output]
        digit_numbers.append(int("".join(map(str, decoded))))
        counter.update(decoded)

print(f"Part 1: {counter[1]+counter[4]+counter[7]+counter[8]}")
print(f"Part 2: {sum(n)}")