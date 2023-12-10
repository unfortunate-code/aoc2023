import math


def solution(file):
    with open(file, "r") as f:
        lines = f.readlines()
    times = list(map(int, lines[0].split(":")[1].strip().split()))
    records = list(map(int, lines[1].split(":")[1].strip().split()))
    res = 1
    for A, B in zip(times, records):
        f = math.floor((A - math.sqrt(A**2 - 4 * B)) / 2) + 1
        res *= A - 2 * f + 1
    return res


print(solution("input.txt"))
