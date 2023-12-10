def solution(file):
    with open(file, "r") as f:
        lr, paths = f.read().split("\n\n")

    d = {
        a: b[1:-1].split(", ")
        for a, b in (line.split(" = ") for line in paths.splitlines())
    }

    s = 0
    curr = "AAA"
    while curr != "ZZZ" and (s := s + 1):
        curr = d[curr][int(lr[(s - 1) % len(lr)] == "R")]
    return s


print(solution("input.txt"))
