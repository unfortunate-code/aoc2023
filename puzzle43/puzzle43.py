def process_input(file):
    with open(file, "r") as f:
        lines = f.read().splitlines()
    bricks = []
    for line in lines:
        s, e = line.split("~")
        s, e = (list(map(int, s.split(","))), list(map(int, e.split(","))))
        if s[-1] > e[-1]:
            s, e = e, s
        bricks.append((s, e))
    return bricks


def solution(file):
    bricks = process_input(file)
    bricks.sort(key=lambda x: x[1][2])
    adj = [[] for _ in range(len(bricks))]
    can = set(range(len(bricks)))

    def has_overlap(b1, b2):
        minx1, maxx1, miny1, maxy1 = (
            min(b1[0][0], b1[1][0]),
            max(b1[0][0], b1[1][0]),
            min(b1[0][1], b1[1][1]),
            max(b1[0][1], b1[1][1]),
        )
        minx2, maxx2, miny2, maxy2 = (
            min(b2[0][0], b2[1][0]),
            max(b2[0][0], b2[1][0]),
            min(b2[0][1], b2[1][1]),
            max(b2[0][1], b2[1][1]),
        )
        return not (minx1 > maxx2 or maxx1 < minx2 or miny1 > maxy2 or maxy1 < miny2)

    for i in range(len(bricks)):
        for j in range(i - 1, -1, -1):
            if has_overlap(bricks[i], bricks[j]):
                adj[i].append(j)

    for i in range(len(bricks)):
        l = bricks[i][1][2] - bricks[i][0][2]
        z = 0
        supports = set()
        for j in adj[i]:
            if z < bricks[j][1][2]:
                z = bricks[j][1][2]
                supports.clear()
            if z == bricks[j][1][2]:
                supports.add(j)
        bricks[i][0][2] = z + 1
        bricks[i][1][2] = z + 1 + l
        if len(supports) == 1:
            support = supports.pop()
            if support in can:
                can.remove(support)

    return len(can)


print(solution("input.txt"))
