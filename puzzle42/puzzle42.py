from collections import deque

STEPS = 5000


def solution(file):
    with open(file, "r") as f:
        lines = f.read().splitlines()

    allowed = set()
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] in ".S":
                allowed.add((i, j))
                if lines[i][j] == "S":
                    start = (i, j)

    def is_allowed(pos):
        i, j = pos
        i = i % len(lines)
        j = j % len(lines[i])
        return (i, j) in allowed

    q = deque()
    q.append((start, 0))
    visited = set()
    visited.add(start)
    count = 0
    while q:
        pos, level = q.popleft()
        if level > 1:
            break
        if level % 2:
            count += 1
        for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_pos = (pos[0] + i, pos[1] + j)
            if is_allowed(new_pos) and new_pos not in visited:
                q.append((new_pos, level + 1))
                visited.add(new_pos)
    print(count)
    return level


print(solution("input.txt"))
