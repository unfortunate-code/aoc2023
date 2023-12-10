from math import comb


def solution(file):
    with open(file, "r") as f:
        lines = [list(map(int, line.split())) for line in f.readlines()]

    def find_next(line):
        n = len(line)
        return sum(((1, -1)[i % 2] * comb(n, i + 1) * line[i] for i in range(n)))

    return sum((find_next(line) for line in lines))


print(solution("input.txt"))
