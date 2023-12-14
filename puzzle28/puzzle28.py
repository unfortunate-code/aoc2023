def solution(file):
    with open(file, "r") as f:
        lines = [list(line) for line in f.read().splitlines()]

    def north():
        for j in range(len(lines[0])):
            pos = 0
            for i in range(len(lines)):
                if lines[i][j] == "#":
                    pos = i + 1
                if lines[i][j] == "O":
                    lines[pos][j], lines[i][j] = lines[i][j], lines[pos][j]
                    pos += 1

    def west():
        for i in range(len(lines)):
            pos = 0
            for j in range(len(lines[0])):
                if lines[i][j] == "#":
                    pos = j + 1
                if lines[i][j] == "O":
                    lines[i][pos], lines[i][j] = lines[i][j], lines[i][pos]
                    pos += 1

    def south():
        for j in range(len(lines[0])):
            pos = len(lines) - 1
            for i in range(len(lines) - 1, -1, -1):
                if lines[i][j] == "#":
                    pos = i - 1
                if lines[i][j] == "O":
                    lines[pos][j], lines[i][j] = lines[i][j], lines[pos][j]
                    pos -= 1

    def east():
        for i in range(len(lines)):
            pos = len(lines[0]) - 1
            for j in range(len(lines[0]) - 1, -1, -1):
                if lines[i][j] == "#":
                    pos = j - 1
                if lines[i][j] == "O":
                    lines[i][pos], lines[i][j] = lines[i][j], lines[i][pos]
                    pos -= 1

    def spin():
        north()
        west()
        south()
        east()

    dp = {}
    idx_map = {}
    total_steps = 1000000000
    loop_length = 0

    def serialize(lines):
        return "\n".join("".join(line) for line in lines)

    for step in range(total_steps):
        A = serialize(lines)
        if A in dp:
            loop_length = step - dp[A][1]
            break
        spin()
        B = serialize(lines)
        dp[A] = B, step
        idx_map[step] = B

    remaining = (total_steps - step) % loop_length

    A = idx_map[dp[A][1] + remaining]

    return sum(
        (len(lines) - i) * line.count("O") for i, line in enumerate(A.splitlines())
    )


print(solution("input.txt"))
