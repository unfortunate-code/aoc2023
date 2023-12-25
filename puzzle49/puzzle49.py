import networkx as nx


def solution(file):
    with open(file) as f:
        lines = f.read().splitlines()

    G = nx.Graph()
    nodes = set()
    for line in lines:
        a, b = line.split(": ")
        nodes.add(a)
        b = b.split(" ")
        for c in b:
            nodes.add(c)
            G.add_edge(a, c, capacity=1)

    nodes = list(nodes)
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            cut_value, partition = nx.minimum_cut(G, nodes[i], nodes[j])
            if cut_value == 3:
                return len(partition[0]) * len(partition[1])


print(solution("input.txt"))
