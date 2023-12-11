from itertools import accumulate


def solution(file):
    with open(file, "r") as f:
        lines = f.readlines()
        rows = [1] * len(lines)
        cols = [1] * len(lines[0].strip("\n"))
    galaxies = []
    for i, line in enumerate(lines):
        for j, c in enumerate(line.strip("\n")):
            if c == "#":
                cols[j] = 0
                rows[i] = 0
                galaxies.append((i, j))
    rows = list(accumulate(rows))
    cols = list(accumulate(cols))
    sum = 0
    for i in range(len(galaxies)):
        X, Y = galaxies[i]
        for j in range(i + 1, len(galaxies)):
            x, y = galaxies[j]
            sum += (
                abs(rows[x] - rows[X])
                + abs(cols[y] - cols[Y])
                + abs(x - X)
                + abs(y - Y)
            )
    return sum


print(solution("input.txt"))
