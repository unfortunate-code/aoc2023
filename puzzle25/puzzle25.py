NUM_SMUDGES = 0


def solution(file):
    with open(file) as f:
        inputs = [input.splitlines() for input in f.read().split("\n\n")]

    def map_to_int(lines):
        return [
            int("".join("1" if c == "#" else "0" for c in line), 2) for line in lines
        ]

    def find_mirror(lines):
        r = map_to_int(lines)
        for i in range(len(r) - 1):
            top, bottom = (
                (r[: i + 1], r[i + 1 : 2 * i + 2])
                if i < len(r) // 2
                else (r[i + 1 - len(r[i + 1 :]) : i + 1], r[i + 1 :])
            )
            if (
                sum(bin(top[j] ^ bottom[~j]).count("1") for j in range(len(top)))
                == NUM_SMUDGES
            ):
                return i
        return -1

    return sum(
        100 * (loc + 1)
        if (loc := find_mirror(lines)) != -1
        else find_mirror(zip(*lines)) + 1
        for lines in inputs
    )


print(solution("input.txt"))
