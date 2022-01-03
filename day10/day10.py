import queue
import numpy as np

def yieldline(infile: str):
    with open(infile, "r") as f:
        for line in f.readlines():
            yield line.strip()

charmap = {")": "(", "]": "[", "}": "{", ">": "<"}
charmap_inv = {value: key for key, value in charmap.items()}
scoremap1 = {")": 3, "]": 57, "}": 1197, ">": 25137}
scoremap2 = {")": 1, "]": 2, "}": 3, ">": 4}

if __name__ == "__main__":    
    score = 0
    scores2 = []
    for line in yieldline("input.txt"):
        q = queue.LifoQueue()
        valid = True
        for char in line:
            if char in charmap.values():
                q.put(char)
            else:
                last_char = q.get()
                if not charmap[char] == last_char: # invalid clsoing character
                    score += scoremap1[char]       
                    valid = False
                    break

        if valid and not q.empty(): # Line valid, but incomplete
            closing = []
            while not q.empty():
                closing.append(charmap_inv[q.get()])
            tmp_score = 0
            for char in closing:
                tmp_score = 5*tmp_score + scoremap2[char]
            scores2.append(tmp_score)
    print("Part1: ", score)
    print("Part2: ", np.median(scores2).astype(int))