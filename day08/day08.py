import numpy as np
from numpy.core.defchararray import count
from numpy.core.fromnumeric import shape
from numpy.lib.arraysetops import unique
from numpy.linalg import inv, pinv
from typing import Generator

def parse_input(filename: str) -> Generator[tuple[list[str], list[str]], None, None]:
    with open(filename, 'r') as f:
        for line in f.readlines():
            # get rid of spaces around the splitting character
            line = line.replace(" | ", "|")
            patterns, output = line.strip().split("|")
            yield patterns.split(" "), output.split(" ")

def index_to_letter(i: int) -> str:
    return chr(ord('a')+i)

def code_to_matrix(codes: list[str]) -> np.array:
    out = np.zeros(shape=(10, 7))
    for row, code in enumerate(codes):
        for i in range(ord('a'), ord('g')+1):
            if chr(i) in code:
                out[row, i-ord('a')] = 1
    return out



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

def code_matrix(M):
    letter_counts = M.sum(axis=0)
    A = np.tile(np.arange(0, 7), 10).reshape(10, 7)
    return letter_counts[A]*M

def P7(M):
    col_idx = M.sum(axis=0).argsort()
    return np.eye(7)[col_idx]

def P10(M):
    col_idx = M.sum(axis=1).argsort()
    return np.eye(10)[col_idx]    

code = code_matrix(M)
print(P10(code)@code@P7(code).T)

for pattern, output in parse_input("testinput.txt"):
    incode = code_matrix(code_to_matrix(pattern))
    print(P10(incode)@incode@P7(incode).T)