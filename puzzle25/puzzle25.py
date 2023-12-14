def solution(file):
    with open(file) as f:
        inputs = f.read().split("\n\n")

    def map_to_int(lines):
        res = [[1 if c == "#" else 0 for c in line] for line in lines]
        return [int("".join(map(str, line)), 2) for line in res]

    def get_number_of_ones(num):
        return bin(num).count("1")

    def num_smudges(top, bottom):
        res = 0
        for i in range(len(top)):
            res += get_number_of_ones(top[i] ^ bottom[i])
        return res

    def find_mirror(lines):
        r = map_to_int(lines)
        for i in range(len(r) - 1):
            if i < len(r) // 2:
                top = r[: i + 1]
                bottom = r[i + 1 : 2 * i + 2]
            else:
                bottom = r[i + 1 :]
                top = r[i + 1 - len(bottom) : i + 1]
            if num_smudges(top, bottom[::-1]) == 0:
                return i
        return -1

    res = 0
    for input in inputs:
        lines = input.splitlines()
        if (loc := find_mirror(lines)) != -1:
            res += 100 * (loc + 1)
        else:
            res += find_mirror(list(zip(*lines))) + 1
    return res


print(solution("input.txt"))
