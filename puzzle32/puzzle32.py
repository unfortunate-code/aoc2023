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

    def num_of_energized_tiles(start, start_direction):
        visited = {}

        q = deque()
        q.append((*start, start_direction))
        visited[start] = set()
        visited[start].add(start_direction)
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

    res = 0
    for j in range(len(lines[0])):
        start = (0, j)
        direction = (1, 0)
        res = max(res, num_of_energized_tiles(start, direction))
        start = (len(lines) - 1, j)
        direction = (-1, 0)
        res = max(res, num_of_energized_tiles(start, direction))

    for i in range(len(lines)):
        start = (i, 0)
        direction = (0, 1)
        res = max(res, num_of_energized_tiles(start, direction))
        start = (i, len(lines[0]) - 1)
        direction = (0, -1)
        res = max(res, num_of_energized_tiles(start, direction))

    return res


print(solution("input.txt"))
