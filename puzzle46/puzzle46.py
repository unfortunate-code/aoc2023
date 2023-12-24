from pprint import pprint


def solution(file):
    with open(file, "r") as f:
        lines = f.read().splitlines()

    adj = {}
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "#":
                continue
            for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if i + d[0] < 0 or i + d[0] >= len(lines):
                    continue
                if j + d[1] < 0 or j + d[1] >= len(lines[i]):
                    continue
                if lines[i + d[0]][j + d[1]] == "#":
                    continue
                if (i, j) not in adj:
                    adj[(i, j)] = []
                adj[(i, j)].append((i + d[0], j + d[1]))

    next = {}
    for k in adj:
        next[k] = []
        for n in adj[k]:
            prev = k
            dist = 1
            v = adj[n]
            while len(v) == 2:
                if v[0] == prev:
                    prev = n
                    n = v[1]
                else:
                    prev = n
                    n = v[0]
                dist += 1
                v = adj[n]
            next[k].append((n, dist))

    def iterative_dfs():
        stack = [(0, lines[0].index("."), 0, set())]
        max_distance = 0
        while stack:
            x, y, dist, visited = stack.pop()
            if x == len(lines) - 1:
                max_distance = max(max_distance, dist)
                continue
            if (x, y) in visited:
                continue
            visited.add((x, y))
            N = next[(x, y)]
            for (nx, ny), d in N:
                stack.append((nx, ny, dist + d, visited.copy()))
        return max_distance

    return iterative_dfs()


print(solution("input.txt"))
