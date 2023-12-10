from collections import deque


def solution(file):
    with open(file, "r") as f:
        lines = [line.strip("\n") for line in f.readlines()]

    def pad(lines):
        new_lines = [["."] * len(lines[0] * 3) for _ in range(len(lines) * 3)]
        total = set()
        for i, line in enumerate(lines):
            for j, c in enumerate(line):
                X = 3 * i + 1
                Y = 3 * j + 1
                total.add((X, Y))
                new_lines[X][Y] = c
                if c == "S":
                    start = (X, Y)
                if c == "-":
                    new_lines[X][Y - 1] = "-"
                    new_lines[X][Y + 1] = "-"
                elif c == "|":
                    new_lines[X - 1][Y] = "|"
                    new_lines[X + 1][Y] = "|"
                elif c == "L":
                    new_lines[X][Y + 1] = "-"
                    new_lines[X - 1][Y] = "|"
                elif c == "J":
                    new_lines[X][Y - 1] = "-"
                    new_lines[X - 1][Y] = "|"
                elif c == "7":
                    new_lines[X][Y - 1] = "-"
                    new_lines[X + 1][Y] = "|"
                elif c == "F":
                    new_lines[X][Y + 1] = "-"
                    new_lines[X + 1][Y] = "|"
        X, Y = start
        start_direction = []
        if X - 2 >= 0 and new_lines[X - 2][Y] == "|":
            new_lines[X - 1][Y] = "|"
            start_direction.append((-1, 0))
        if X + 2 < len(new_lines) and new_lines[X + 2][Y] == "|":
            new_lines[X + 1][Y] = "|"
            start_direction.append((1, 0))
        if Y - 2 >= 0 and new_lines[X][Y - 2] == "-":
            new_lines[X][Y - 1] = "-"
            start_direction.append((0, -1))
        if Y + 2 < len(new_lines[0]) and new_lines[X][Y + 2] == "-":
            new_lines[X][Y + 1] = "-"
            start_direction.append((0, 1))
        return new_lines, (X, Y), start_direction, total

    lines, start, start_direction, total = pad(lines)
    directions = {
        "S": start_direction,
        "-": [(0, 1), (0, -1)],
        "|": [(1, 0), (-1, 0)],
        "L": [(0, 1), (-1, 0)],
        "J": [(0, -1), (-1, 0)],
        "7": [(1, 0), (0, -1)],
        "F": [(1, 0), (0, 1)],
    }
    q = deque()
    q.append(start)
    path = set()
    path.add(start)
    total.remove(start)
    while q:
        pos = q.popleft()
        for direction in directions[lines[pos[0]][pos[1]]]:
            new_pos = (pos[0] + direction[0], pos[1] + direction[1])
            if new_pos not in path:
                q.append(new_pos)
                path.add(new_pos)
                if new_pos in total:
                    total.remove(new_pos)
    q.append((0, 0))
    visited = set()
    while q:
        pos = q.popleft()
        for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_pos = (pos[0] + direction[0], pos[1] + direction[1])
            if (
                new_pos[0] < 0
                or new_pos[0] >= len(lines)
                or new_pos[1] < 0
                or new_pos[1] >= len(lines[0])
            ):
                continue
            if new_pos not in path and new_pos not in visited:
                q.append(new_pos)
                visited.add(new_pos)
                if new_pos in total:
                    total.remove(new_pos)
    return len(total)


print(solution("input.txt"))
