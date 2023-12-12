from functools import cache


def parse_file(file):
    with open(file, "r") as f:
        return [line.split() for line in f]


def count_hashes(pattern):
    count = 0
    for char in reversed(pattern):
        if char == "#":
            count += 1
        yield count


def solution(file):
    def count(pattern, rule):
        pattern = ((pattern + "?") * 5)[:-1]
        freq = list(count_hashes(pattern))[::-1]
        rule = list(map(int, rule.split(","))) * 5

        @cache
        def inner(i_r, i_p, curr):
            if i_r == len(rule) and (i_p == len(pattern) or freq[i_p] == 0):
                return 1
            if i_r == len(rule) - 1 and i_p == len(pattern) and curr == rule[i_r]:
                return 1
            if i_r == len(rule) or i_p == len(pattern):
                return 0

            if pattern[i_p] in ".#":
                if curr == rule[i_r]:
                    if pattern[i_p] == "#":
                        return 0
                    i_r += 1
                    curr = 0
                if pattern[i_p] == "." and 0 < curr < rule[i_r]:
                    return 0
                curr += pattern[i_p] == "#"
                return inner(i_r, i_p + 1, curr)
            else:
                if curr == rule[i_r]:
                    return inner(i_r + 1, i_p + 1, 0)
                if 0 < curr < rule[i_r]:
                    return inner(i_r, i_p + 1, curr + 1)
                return inner(i_r, i_p + 1, 1) + inner(i_r, i_p + 1, 0)

        return inner(0, 0, 0)

    patterns_rules = parse_file(file)
    return sum(count(pattern, rule) for pattern, rule in patterns_rules)


print(solution("input.txt"))
