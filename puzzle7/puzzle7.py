def solution(file):
    with open(file, 'r') as f:
        lines = f.readlines()
    sum = 0
    def common(a, b):
        count = 0
        for x in b:
            if x in a:
                count += 1
        return count
    
    for line in lines:
        winning, have = line.split(': ')[1].split(' | ')
        winning = set(winning.strip().split())
        have = have.strip().split()
        count = common(winning, have)
        if count > 0:
            sum += 1 << (count - 1)
    return sum

print(solution('input.txt'))