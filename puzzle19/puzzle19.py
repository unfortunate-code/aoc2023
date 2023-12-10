from collections import deque


def solution(file):
    with open(file, "r") as f:
        lines = f.readlines()
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    possibles = [set("-7J"), set("|LJ"), set("FL-"), set("|F7")]
    for i, line in enumerate(lines):
        if "S" in line:
            start = (i, line.index("S"))
    q = deque()
    visited = set()
    visited.add(start)
    res = 0
    for i, direction in enumerate(directions):
        pos = (start[0] + direction[0], start[1] + direction[1])
        if lines[pos[0]][pos[1]] in possibles[i]:
            q.append((pos, 1))
            visited.add(pos)
            res = 1

    directions = {
        "-": [(0, 1), (0, -1)],
        "|": [(1, 0), (-1, 0)],
        "L": [(0, 1), (-1, 0)],
        "J": [(0, -1), (-1, 0)],
        "7": [(1, 0), (0, -1)],
        "F": [(1, 0), (0, 1)],
    }
    while q:
        pos, step = q.popleft()
        for direction in directions[lines[pos[0]][pos[1]]]:
            new_pos = (pos[0] + direction[0], pos[1] + direction[1])
            if new_pos not in visited:
                res = max(res, step + 1)
                q.append((new_pos, step + 1))
                visited.add(new_pos)
    return res


print(solution("input.txt"))
