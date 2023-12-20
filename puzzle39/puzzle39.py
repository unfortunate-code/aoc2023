from collections import deque


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

    def press_button():
        q = deque()
        pulses_count = [0, 0]
        q.append((False, nodes["broadcaster"], None))
        while q:
            signal, node, parent = q.popleft()
            pulses_count[signal] += 1
            signal, children = node.process(signal, parent)
            for child in children:
                q.append((signal, nodes[child], node.name))

        return pulses_count

    pulses_count_list = []
    for _ in range(1000):
        pulses_count_list.append(press_button())
        if all(node.is_reset() for node in nodes.values()):
            break

    q, r = divmod(1000, len(pulses_count_list))
    lows, highs = zip(*pulses_count_list)
    rlows = lows[:r]
    rhighs = highs[:r]
    return (sum(lows) * q + sum(rlows)) * (sum(highs) * q + sum(rhighs))


print(solution("input.txt"))
