import numpy as np
from collections import defaultdict, Counter


def build_graph(filename: str) -> dict[str, list[str]]:
    """
    Nuild graph using a dictionary with a list of adjacent nodes as values
    """
    with open(filename, "r") as infile:
        # input file contains a list of edges
        edges = [line.strip().split("-") for line in infile.readlines()]
        graph = defaultdict(list)
        for edge in edges:
            e1, e2 = edge
            graph[e1].append(e2)
            graph[e2].append(e1)
        return graph


def find_paths(
    graph: dict[str, list[str]],
    start: str = "start",
    end: str = "end",
    path: list = None,
    allow_twice: bool = False,
):
    """
    Find all paths from "start" to "end" using depth first search
    """
    if path is None:
        path = [start]
    else:
        path = path + [start]
    if start == end:
        return [path]
    paths = []
    for vertex in graph[start]:
        # lower letter vertices can be only visited once,  while capital letter
        # letters can be visited multiple times
        if (vertex.islower() and vertex not in path) or vertex.isupper():
            newpaths = find_paths(graph, vertex, "end", path, allow_twice)
        elif vertex.islower() and allow_twice and vertex not in ["start", "stop"]:
            newpaths = find_paths(graph, vertex, "end", path, False)
        else:
            newpaths = []
        for newpath in newpaths:
            paths.append(newpath)
    return paths


graph = build_graph("input.txt")
p = find_paths(graph)
print("Part 1:", len(p))
p = find_paths(graph, allow_twice=True)
print("Part 2:", len(p))
