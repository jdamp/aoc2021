import re
import networkx as nx

def apply_rule(rule, weight):
    """
    Replace e0->e1 with e0->e2, e2->e1
    """
    (e0, e1), e2 = rule
    return [[e0, e2, {'weight': weight}], [e2, e1, {'weight': weight}]]

def add_edges_count_weight(g, edges):
    for edge in edges:
        n0, n1, data = edge
        if g.has_edge(n0, n1):
            g[n0][n1]['weight'] += data["weight"]
        else:
            g.add_edge(n0, n1, weight=data["weight"])
    return g

def get_node_diff(graph):
    """
    Calculate the difference between the most common and the least common letter in the polymer graph

    The total occurence of each letter in the polymer graph is directly related to the numbers
    of edges of a given node.
    For letters occuring at the first or last position in the polymer, the number of outgoing and incoming
    nodes will differ by one, the maximum is taken in this case.
    For all others, both will be the same.
    """
    node_counts = {}
    for node in gnew.nodes():
        node_counts_in = sum([data['weight'] for _, __, data in gnew.in_edges(node, data=True)])
        node_counts_out = sum([data['weight'] for _, __, data in gnew.out_edges(node, data=True)])
        node_counts[node] = max(node_counts_in, node_counts_in)
    sorted_counts = sorted(node_counts.values())
    return sorted_counts[-1] - sorted_counts[0]

with open("input.txt", "r") as f:
    lines = f.readlines()
    polymer = lines[0].strip()
    polymer_edges = [(polymer[i], polymer[i+1]) for i in range(len(polymer)-1)]
    rulestr = lines[2:]
    rules = [re.search("([A-Z]+) -> ([A-Z])", rule.strip()).groups() for rule in rulestr]

g0 = nx.DiGraph()
for edge in polymer_edges:
    g0.add_edge(*edge, weight=1)

for step in range(1, 41):
    gnew = nx.DiGraph()
    for rule in rules:
        if not tuple(rule[0]) in g0.edges(): # rule does not apply to graph
            continue
        for e0, e1, weight in g0.edges(data="weight"):
            if not tuple(rule[0]) == (e0, e1): # rule does not apply to this node
                continue
            gnew = add_edges_count_weight(gnew, apply_rule(rule, weight))
    g0 = gnew
    if step == 10: 
        print("Part 1:", get_node_diff(gnew))

print("Part 2:", get_node_diff(gnew))