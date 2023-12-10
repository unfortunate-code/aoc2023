from functools import reduce
from math import lcm


def solution(file):
    with open(file, "r") as f:
        lr, paths = f.read().split("\n\n")

    d = {
        a: b[1:-1].split(", ")
        for a, b in (line.split(" = ") for line in paths.splitlines())
    }

    def length(curr):
        s = 0
        while curr[-1] != "Z" and (s := s + 1):
            curr = d[curr][int(lr[(s - 1) % len(lr)] == "R")]
        return s

    return reduce(lcm, (length(start) for start in d if start[-1] == "A"))


print(solution("input.txt"))
