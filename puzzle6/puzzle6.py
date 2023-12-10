from collections import defaultdict


def solution(file):
    with open(file, "r") as f:
        lines = f.readlines()
    sum = 0
    d = defaultdict(dict)
    for i in range(len(lines)):
        line = lines[i].strip()
        j = 0
        while j < len(line):
            if line[j] == ".":
                j += 1
            elif "0" <= line[j] <= "9":
                k = j + 1
                while k < len(line) and "0" <= line[k] <= "9":
                    k += 1
                d[i][j] = (k - 1, int(line[j:k]))
                j = k
            else:
                d[i][j] = (j, -1)
                j += 1
    for i, v in d.items():
        prev = (-2, 0)
        for l, (r, n) in v.items():
            if n > 0:
                prev = (r, n)
                continue
            total = 0
            prod = 1
            if prev[0] == l - 1:
                total += 1
                prod *= prev[1]
            if l + 1 in v:
                total += 1
                prod *= v[l + 1][1]
            for j in [i - 1, i + 1]:
                if total > 2:
                    break
                if j in d:
                    for s in d[j]:
                        e, m = d[j][s]
                        if m == -1:
                            continue
                        if s - 1 <= l <= e + 1:
                            total += 1
                            if total > 2:
                                break
                            prod *= m
            if total == 2:
                sum += prod
    return sum


print(solution("input.txt"))
