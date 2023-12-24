def solution(file):
    with open(file, "r") as f:
        lines = f.read().splitlines()

    directions = {
        ".": [(0, 1), (1, 0), (0, -1), (-1, 0)],
        ">": [(0, 1)],
        "<": [(0, -1)],
        "^": [(-1, 0)],
        "v": [(1, 0)],
    }

    def iterative_dfs():
        stack = [(0, lines[0].index("."), 0, set())]  # x, y, distance, visited_copy
        max_distance = 0
        while stack:
            x, y, dist, visited_copy = stack.pop()
            if x == len(lines) - 1:
                max_distance = max(max_distance, dist)
                continue
            if (x, y) in visited_copy:
                continue
            visited_copy.add((x, y))
            for dx, dy in directions[lines[x][y]]:
                nx, ny = x + dx, y + dy
                if (
                    0 <= nx < len(lines)
                    and 0 <= ny < len(lines[0])
                    and (nx, ny) not in visited_copy
                    and lines[nx][ny] != "#"
                ):
                    stack.append((nx, ny, dist + 1, visited_copy.copy()))
        return max_distance

    return iterative_dfs()


print(solution("input.txt"))
