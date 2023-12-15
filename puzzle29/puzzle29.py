def solution(file):
    def hash(s):
        s = [ord(c) for c in s]
        curr = 0
        for x in s:
            curr += x
            curr *= 17
            curr %= 256
        return curr

    with open(file, "r") as f:
        return sum(hash(s) for s in f.read().strip().split(","))


print(solution("input.txt"))
