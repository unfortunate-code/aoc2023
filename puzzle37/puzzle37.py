class DecisionNode:
    def __init__(self, name):
        self.name = name

    def set_conds(self, conds, node_map):
        conds = conds.split(",")
        self.children = []
        for cond in conds:
            if ":" in cond:
                cond, next = cond.split(":")
                if "<" in cond:
                    c, i = cond.split("<")
                    i = int(i)
                    self.children.append(({c: (1, i - 1)}, node_map[next]))
                else:
                    c, i = cond.split(">")
                    i = int(i)
                    self.children.append(({c: (i + 1, 4000)}, node_map[next]))
            else:
                self.children.append(({}, node_map[cond]))

    def next(self, part):
        for cond, next in self.children:
            for k, v in cond.items():
                if part[k] < v[0] or part[k] > v[1]:
                    break
            else:
                return next.name

    def is_accepted(self):
        return self.name == "A"

    def is_rejected(self):
        return self.name == "R"


def solution(file):
    with open(file, "r") as f:
        workflows, parts = f.read().split("\n\n")

    workflows = [w.split("{") for w in workflows.splitlines()]
    workflows = {w[0]: w[1][:-1] for w in workflows}
    node_map = {k: DecisionNode(k) for k in workflows.keys()}
    node_map["A"] = DecisionNode("A")
    node_map["R"] = DecisionNode("R")

    for k, v in workflows.items():
        node_map[k].set_conds(v, node_map)

    parts = [p[1:-1].split(",") for p in parts.splitlines()]
    parts = [{k: int(v) for k, v in [p.split("=") for p in part]} for part in parts]

    res = 0
    for part in parts:
        node = "in"
        while not node_map[node].is_accepted() and not node_map[node].is_rejected():
            node = node_map[node].next(part)
        if node_map[node].is_accepted():
            res += sum(part.values())
    return res


print(solution("input.txt"))
