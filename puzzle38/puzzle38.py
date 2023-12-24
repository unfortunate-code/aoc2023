import re
from copy import deepcopy


class PartRange:
    def __init__(self, ranges=None):
        self.ranges = deepcopy(ranges) or {l: [0, 4001] for l in "xmas"}

    def splitOn(self, lhs):
        inRange = PartRange(self.ranges)
        outRange = PartRange(self.ranges)
        num = int(lhs[2:])

        existingRange = inRange.ranges[lhs[0]]
        if existingRange[0] <= num <= existingRange[1]:
            if lhs[1] == ">":
                inRange.ranges[lhs[0]][0] = num
                outRange.ranges[lhs[0]][1] = num + 1
            else:  # <
                inRange.ranges[lhs[0]][1] = num
                outRange.ranges[lhs[0]][0] = num - 1
        elif num < existingRange[0] and lhs[1] == ">":
            outRange = None
        elif num > existingRange[1] and lhs[1] == "<":
            outRange = None
        else:
            inRange = outRange = None
        return inRange, outRange

    def score(self):
        ans = 1
        for l, h in self.ranges.values():
            ans *= h - l - 1
        return ans

    def inRange(self, *args):
        for l, v in zip("xmas", args):
            if not self.ranges[l][0] < v < self.ranges[l][1]:
                return False
        return True


def solution(file):
    with open(file, "r") as f:
        workflows = f.read().split("\n\n")[0]

    workflows = [w.split("{") for w in workflows.splitlines()]
    workflows = {w[0]: w[1][:-1].split(",") for w in workflows}

    validRanges = []

    def testRange(partRange, name):
        if partRange is None:
            return
        if name in "AR":
            if name == "A":
                validRanges.append(partRange)
        else:
            rules = workflows[name]
            for r in rules:
                if ":" not in r:
                    testRange(partRange, r)
                else:
                    lhs, next = r.split(":")
                    inR, outR = partRange.splitOn(lhs)
                    testRange(inR, next)
                    partRange = outR
                    if partRange == None:
                        return

    testRange(PartRange(), "in")

    return sum(pr.score() for pr in validRanges)
