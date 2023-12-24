from collections import deque

STEPS = 64


def solution(file):
    with open(file, "r") as f:
        lines = f.read().splitlines()

    allowed = set()
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == ".":
                allowed.add((i, j))
            elif lines[i][j] == "S":
                start = (i, j)

    q = deque()
    q.append((start, 0))
    visited = set()
    visited.add(start)
    count = 0
    while q:
        pos, level = q.popleft()
        if level % 2 == 0:
            count += 1
        if level > STEPS:
            break
        for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_pos = (pos[0] + i, pos[1] + j)
            if new_pos in allowed and new_pos not in visited:
                q.append((new_pos, level + 1))
                visited.add(new_pos)
    return count


print(solution("input.txt"))
