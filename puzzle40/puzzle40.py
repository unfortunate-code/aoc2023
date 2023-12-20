from collections import deque
from math import lcm

import matplotlib.pyplot as plt
import networkx as nx


class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parents = []
        self.type = None
        self.default_state = None
        self.state = None

    def initialize(self):
        if self.type == "%":
            self.default_state = False
            self.state = False
        elif self.type == "&":
            self.default_state = [False] * len(self.parents)
            self.state = [False] * len(self.parents)

    def is_reset(self):
        return self.state == self.default_state

    def __repr__(self):
        return f"{self.name}: {self.children}"

    def process(self, signal, parent):
        if self.type == "broadcaster":
            return signal, self.children
        elif self.type == "%":
            if signal:
                return signal, []
            else:
                self.state = not self.state
                return self.state, self.children
        elif self.type == "&":
            self.state[self.parents.index(parent)] = signal
            return not all(self.state), self.children
        return signal, self.children


def solution(file):
    with open(file, "r") as f:
        lines = f.read().splitlines()

    nodes = {}
    for line in lines:
        parent, children = line.split(" -> ")
        children = children.split(", ")
        if parent == "broadcaster":
            type = parent
        else:
            type = parent[0]
            parent = parent[1:]
        if parent not in nodes:
            nodes[parent] = Node(parent)
        nodes[parent].type = type
        nodes[parent].children = children
        for child in children:
            if child not in nodes:
                nodes[child] = Node(child)
            nodes[child].parents.append(parent)

    for node in nodes.values():
        node.initialize()

    def press_button(till):
        q = deque()
        q.append((False, nodes["broadcaster"], None))
        pos = 0
        neg = 0
        while q:
            signal, node, parent = q.popleft()
            if node.name == till:
                if signal:
                    pos += 1
                else:
                    neg += 1
            signal, children = node.process(signal, parent)
            for child in children:
                q.append((signal, nodes[child], node.name))
        return neg == 1

    def plot_graph():
        def name(node):
            if node.type == "broadcaster":
                return "B"
            return node.name

        adj = {name(node): node.children for node in nodes.values()}
        G = nx.DiGraph(adj)
        for node, neighbors in adj.items():
            for neighbor in neighbors:
                G.add_edge(node, neighbor)

        labels = {
            name(node): name(node) if node.type != "&" else name(node).upper()
            for node in nodes.values()
        }
        nx.draw(G, with_labels=True, labels=labels)
        plt.show()

    # plot_graph()

    def analyze_loops():
        locs = {}
        for node in nodes["vr"].parents:
            for n in nodes.values():
                n.initialize()
            for i in range(100000):
                if press_button(node):
                    locs.setdefault(node, [])
                    locs[node].append(i + 1)
                    if len(locs[node]) > 3:
                        locs[node].pop()
                        break
        print(locs)
        for k in locs:
            v = locs[k]
            v_ = []
            for i in range(len(v) - 1):
                v_.append(v[i + 1] - v[i])
            locs[k] = v_
        print(locs)

    # analyze_loops()

    locs = {}
    for node in nodes["vr"].parents:
        for n in nodes.values():
            n.initialize()
        for i in range(100000):
            if press_button(node):
                locs[node] = i + 1
                break

    return lcm(*locs.values())


print(solution("input.txt"))
