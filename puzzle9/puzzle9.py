from bisect import bisect_left, bisect_right

def solution(file):
    with open(file, 'r') as f:
        lines = f.readlines()
    
    mode_changed = False

    def update(input, output, source, dest, range_val):
        l = bisect_left(input, source)
        r = bisect_right(input, source + range_val - 1)
        for i in range(l, r):
            output[i] = dest + input[i] - source

    for line in lines:
        if line.startswith('seeds'):
            output = [int(x) for x in line.split(': ')[1].split()]
        elif 'map' in line:
            mode_changed = True
        elif line == '\n':
            continue
        else:
            if mode_changed:
                output.sort()
                input = list(output)
                mode_changed = False
            dest, source, range_val = [int(x) for x in line.split()]
            update(input, output, source, dest, range_val)
    return min(output)

print(solution('input.txt'))
            
            
