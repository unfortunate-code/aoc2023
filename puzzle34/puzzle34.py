import heapq


def solution(file):
    with open(file, "r") as f:
        lines = f.read().splitlines()
    q = []
    heapq.heappush(q, (0, (0, 0), (0, 1), 1))
    heapq.heappush(q, (0, (0, 0), (1, 0), 1))
    visited = {}
    visited[((0, 0), None, 0)] = 0
    res = float("inf")
    while q:
        h, n, d, c = heapq.heappop(q)
        nn = (n[0] + d[0], n[1] + d[1])
        if nn == (0, 0):
            continue
        nh = h + int(lines[nn[0]][nn[1]])
        if nh > res:
            continue
        if (nn, d, c) in visited and visited[(nn, d, c)] <= nh:
            continue
        visited[(nn, d, c)] = nh
        if nn == (len(lines) - 1, len(lines[0]) - 1):
            if c >= 4:
                res = min(res, nh)
            continue
        for nd in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nc = 1
            if nd == d:
                if c == 10:
                    continue
                nc = c + 1
            elif c < 4:
                continue
            if (nd[0] and nd[0] == -d[0]) or (nd[1] and nd[1] == -d[1]):
                continue
            nnn = (nn[0] + max(1, 5 - nc) * nd[0], nn[1] + max(1, 5 - nc) * nd[1])
            if (
                nnn[0] < 0
                or nnn[0] >= len(lines)
                or nnn[1] < 0
                or nnn[1] >= len(lines[0])
            ):
                continue
            heapq.heappush(q, (nh, nn, nd, nc))
    return res


print(solution("input.txt"))
