def solution(file):
    with open(file, 'r') as f:
        lines = f.readlines()

    def common(a, b):
        count = 0
        for x in b:
            if x in a:
                count += 1
        return count
    
    res = [1] * len(lines)
    for i, line in enumerate(lines):
        winning, have = line.split(': ')[1].split(' | ')
        winning = set(winning.strip().split())
        have = have.strip().split()
        count =  common(winning, have)
        for j in range(i + 1, min(i + count + 1, len(res))):
            res[j] += res[i]
    return sum(res)

print(solution('input.txt'))