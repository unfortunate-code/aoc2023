from itertools import accumulate


def solution(file, expansion):
    with open(file, "r") as f:
        lines = [line.strip() for line in f]
    rows = [expansion - 1] * len(lines)
    cols = [expansion - 1] * len(lines[0])
    galaxies = []
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == "#":
                cols[j] = 0
                rows[i] = 0
                galaxies.append((i, j))
    rows = list(accumulate(rows))
    cols = list(accumulate(cols))

    X, Y = zip(*[(x + rows[x], y + cols[y]) for x, y in galaxies])
    X, Y = sorted(X), sorted(Y)
    n = len(X)
    return (
        2 * sum(i * x for i, x in enumerate(X))
        + 2 * sum(i * y for i, y in enumerate(Y))
        - (n - 1) * (sum(X) + sum(Y))
    )


print(solution("input.txt", 2))
