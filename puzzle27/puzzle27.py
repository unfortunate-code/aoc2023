def solution(file):
    with open(file, "r") as f:
        lines = f.read().splitlines()

    res = 0
    for j in range(len(lines[0])):
        pos = 0
        for i in range(len(lines)):
            if lines[i][j] == "#":
                pos = i + 1
            if lines[i][j] == "O":
                res += len(lines) - pos
                pos += 1
    return res


print(solution("input.txt"))
