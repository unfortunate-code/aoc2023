import numpy as np


def solution(file, m, M):
    with open(file, "r") as f:
        lines = f.read().splitlines()

    inputs = []
    for line in lines:
        p, v = line.split(" @ ")
        px, py = list(map(int, p.split(",")[:2]))
        vx, vy = list(map(int, v.split(",")[:2]))
        inputs.append([px, py, vx, vy])

    def intersect(px1, py1, vx1, vy1, px2, py2, vx2, vy2):
        # No collision needs to happen. Just check if these two lines intersect at some point with the given bounds of m and M. Return True if they intersect
        p = np.array([px1, py1])
        r = np.array([vx1, vy1])
        q = np.array([px2, py2])
        s = np.array([vx2, vy2])
        rxs = np.cross(r, s)
        if rxs == 0:
            return False
        t = np.cross(q - p, s) / rxs
        u = np.cross(q - p, r) / rxs
        if t < 0 or u < 0:
            return False
        return (
            np.max(p + t * r) <= M
            and np.min(p + t * r) >= m
            and np.max(q + u * s) <= M
            and np.min(q + u * s) >= m
        )

    count = 0
    for i in range(len(inputs)):
        for j in range(i + 1, len(inputs)):
            px1, py1, vx1, vy1 = inputs[i]
            px2, py2, vx2, vy2 = inputs[j]
            count += intersect(px1, py1, vx1, vy1, px2, py2, vx2, vy2)
    return count


print(solution("input.txt", 200000000000000, 400000000000000))
