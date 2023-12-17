from collections import deque


def solution(file):
    with open(file, "r") as f:
        lines = f.read().splitlines()
    directions = {
        ".": {(0, 1): (0, 1), (0, -1): (0, -1), (1, 0): (1, 0), (-1, 0): (-1, 0)},
        "|": {
            (1, 0): (1, 0),
            (-1, 0): (-1, 0),
            (0, 1): [(1, 0), (-1, 0)],
            (0, -1): [(1, 0), (-1, 0)],
        },
        "-": {
            (0, 1): (0, 1),
            (0, -1): (0, -1),
            (1, 0): [(0, 1), (0, -1)],
            (-1, 0): [(0, 1), (0, -1)],
        },
        "/": {(0, 1): (-1, 0), (0, -1): (1, 0), (1, 0): (0, -1), (-1, 0): (0, 1)},
        "\\": {(0, 1): (1, 0), (0, -1): (-1, 0), (1, 0): (0, 1), (-1, 0): (0, -1)},
    }
    visited = {}

    q = deque()
    q.append((0, 0, (0, 1)))
    visited[(0, 0)] = set()
    visited[(0, 0)].add((0, 1))
    while q:
        x, y, d = q.popleft()
        next = directions[lines[x][y]][d]
        if not isinstance(next, list):
            next = [next]
        for n in next:
            nx, ny = x + n[0], y + n[1]
            if 0 <= nx < len(lines) and 0 <= ny < len(lines[0]):
                if (nx, ny) not in visited:
                    visited[(nx, ny)] = set()
                if n not in visited[(nx, ny)]:
                    visited[(nx, ny)].add(n)
                    q.append((nx, ny, n))
    return len(visited)


print(solution("input.txt"))
