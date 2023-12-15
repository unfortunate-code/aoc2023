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
        input = f.read().strip().split(",")

    d = [[] for _ in range(256)]
    for s in input:
        if s[-1] == "-":
            l = d[hash(s[:-1])]
            for x in l:
                if x[0] == s[:-1]:
                    l.remove(x)
                    break
        else:
            label, focus = s.split("=")
            l = d[hash(label)]
            for i, x in enumerate(l):
                if x[0] == label:
                    l[i] = (label, int(focus))
                    break
            else:
                l.append((label, int(focus)))

    res = 0
    for i, box in enumerate(d):
        for j, (label, focus) in enumerate(box):
            res += (i + 1) * (j + 1) * focus
    return res


print(solution("input.txt"))
