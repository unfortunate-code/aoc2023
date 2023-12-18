import re


def solution(file):
    with open(file, "r") as f:
        lines = f.read().splitlines()

    REGEX = r"(\w) (\d+) \((#\w+)\)"
    vertices = [(0, 0)]
    directions = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
    dir_map = {"0": "R", "1": "D", "2": "L", "3": "U"}
    perimeter = 0
    for line in lines:
        color = re.findall(REGEX, line)[0][-1]
        direction = dir_map[color[-1]]
        distance = int("0x" + color[1:6], 16)
        start = vertices[-1]
        end = (
            start[0] + distance * directions[direction][0],
            start[1] + distance * directions[direction][1],
        )
        vertices.append(end)
        perimeter += distance
    xs, ys = zip(*vertices)
    # Not sure how this works. Using Pick's theorem and shoelace formula.
    inner_area = 0.5 * abs(
        sum(i * j for i, j in zip(xs, ys[1:] + ys[:1]))
        - sum(i * j for i, j in zip(xs[1:] + xs[:1], ys))
    )
    return int(inner_area) + perimeter // 2 + 1


print(solution("input.txt"))
