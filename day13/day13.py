import numpy as np
import re

with open("input.txt", "r") as infile:
    text = infile.read()
    dotstr, instructions = text.split("\n\n")
    dots = np.genfromtxt(dotstr.split("\n"), delimiter=",", dtype=np.int32)
shape = np.max(dots, axis=0)+1
paper = np.zeros(shape, dtype=np.int32)
# use 1s as dots
paper[dots[:,0], dots[:,1]] = 1

for i, instruction in enumerate(instructions.split("\n")):
    ax, val = re.search("([xy])=(\d+)", instruction).groups()
    val = int(val)
    if ax == 'x':
        left, foldline, right = np.split(paper, [val, val+1], 0)
        paper = left | right[::-1,:]
    if ax == 'y':
        upper, foldline, lower = np.split(paper, [val, val+1], 1)
        paper = upper | lower[:,::-1]
    if i == 0:
        print("Part 1:", paper.sum())
np.set_printoptions(linewidth=200)
print(np.array2string(paper.T, separator="", 
                      formatter={'int': lambda x: ' ' if x==0 else '█'}))