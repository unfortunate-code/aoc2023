from functools import cache


def solution(file):
    patterns, rules = [], []
    with open(file, "r") as f:
        for line in f:
            p, r = line.split()
            patterns.append(((p + "?") * 5)[:-1])
            rules.append(list(map(int, r.split(","))) * 5)

    def count(p, r):
        freq = [0] * len(p)
        freq[-1] = 1 if p[-1] == "#" else 0
        for i in range(len(p) - 1):
            j = len(p) - i - 2
            if p[j] == "#":
                freq[j] = freq[j + 1] + 1
            else:
                freq[j] = freq[j + 1]

        @cache
        def inner(i_r, i_p, flip):
            if i_r == len(r) and (i_p == len(p) or freq[i_p] == 0):
                return 1
            if i_r == len(r):
                return 0
            if i_p == len(p):
                return 0
            curr = 0
            while i_p < len(p) and i_r < len(r):
                if p[i_p] == ".":
                    i_p += 1
                    if curr == r[i_r]:
                        return inner(i_r + 1, i_p, False)
                    elif 0 < curr < r[i_r]:
                        return 0
                    curr = 0
                elif flip or p[i_p] == "#":
                    flip = False
                    i_p += 1
                    curr += 1
                    if curr > r[i_r]:
                        return 0
                elif p[i_p] == "?":
                    if curr == r[i_r]:
                        return inner(i_r + 1, i_p + 1, False)
                    elif 0 < curr < r[i_r]:
                        i_p += 1
                        curr += 1
                    else:
                        return inner(i_r, i_p, True) + inner(i_r, i_p + 1, False)
            if curr != r[i_r]:
                return 0
            return inner(i_r + 1, i_p, False)

        return inner(0, 0, False)

    return sum(count(p, r) for p, r in zip(patterns, rules))


print(solution("input.txt"))
