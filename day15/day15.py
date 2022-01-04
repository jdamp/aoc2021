import numpy as np
import networkx as nx
from networkx.algorithms.shortest_paths.weighted import single_source_dijkstra

cave = np.genfromtxt("input.txt", delimiter=1, dtype=np.int32)

def build_graph(cave):
    edges = []
    for ix in range(cave.shape[1]):
        for iy in range(cave.shape[0]):
            if ix > 0:
                edges.append([(ix, iy), (ix-1, iy), {'weight': cave[iy, ix-1]}])
            if ix < cave.shape[1] - 1:
                edges.append([(ix, iy), (ix+1, iy), {'weight': cave[iy, ix+1]}])
            if iy > 0:
                edges.append([(ix, iy), (ix, iy-1), {'weight': cave[iy-1, ix]}])
            if iy < cave.shape[0] - 1:
                edges.append([(ix, iy), (ix, iy+1), {'weight': cave[iy+1, ix]}])
    return nx.DiGraph(edges)

def add_wrap(cave, n):
    cave = cave + n
    cave[cave >= 10] = (cave[cave >= 10] % 10) + 1
    return cave

g = build_graph(cave)
risk, path = single_source_dijkstra(g, (0,0), (cave.shape[0]-1, cave.shape[1]-1))
print(f"Part 1: {risk}")
blocks = {i: add_wrap(cave, i) for i in range(9)}

large_cave = np.zeros((5*cave.shape[0], 5*cave.shape[1]))
for ix in range(5):
    for iy in range(5):
        large_cave[iy*cave.shape[1]:(iy+1)*cave.shape[0], ix*cave.shape[0]:(ix+1)*cave.shape[0]] = blocks[ix+iy]

g2 = build_graph(large_cave)
risk, path = single_source_dijkstra(g2, (0,0), (large_cave.shape[0]-1, large_cave.shape[1]-1))
print(f"Part 2: {risk}")