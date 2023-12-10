import math

def solution(file):
    with open(file, 'r') as f:
        lines = f.readlines()
    A = int(''.join(lines[0].split(':')[1].strip().split()))
    B = int(''.join(lines[1].split(':')[1].strip().split()))
    f = math.floor((A - math.sqrt(A**2 - 4*B)) / 2) + 1
    return A - 2*f + 1

print(solution('input.txt'))