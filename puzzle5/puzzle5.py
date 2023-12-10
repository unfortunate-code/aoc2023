from collections import defaultdict

def solution(file):
    with open(file, 'r') as f:
        lines = f.readlines()
    sum = 0
    d = defaultdict(dict)
    for i in range(len(lines)):
        line = lines[i].strip()
        j = 0
        while j < len(line):
            if line[j] == '.':
                j += 1
            elif '0' <= line[j] <= '9':
                k = j + 1
                while k < len(line) and '0' <= line[k] <= '9':
                    k += 1
                d[i][(j, k -1)] = int(line[j:k])
                j = k
            else:
                d[i][(j, j)] = -1
                j += 1
    for i, v in d.items():
        for (l, r), x in v.items():
            if x == -1:
                continue
            if (l - 1, l - 1) in v:
                sum += x
                continue
            if (r + 1, r + 1) in v:
                sum += x
                continue
            if (i - 1) in d:
                for prev in d[i - 1]:
                    if prev[0] == prev[1] and l - 1 <= prev[0] <= r + 1 and d[i - 1][prev] == -1:
                        sum += x
                        break
            if (i + 1) in d:
                for next in d[i + 1]:
                    if next[0] == next[1] and l - 1 <= next[0] <= r + 1 and d[i + 1][next] == -1:
                        sum += x
                        break
        
    return sum

print(solution('input.txt'))
             

