def solution(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        sum = 0
        for line in lines:
            draws = line.split(':')[1]
            draws = draws.split(';')
            min_ = {'red': 0, 'green': 0, 'blue': 0}
            for draw in draws:
                draw = draw.strip()
                colors = draw.split(',')
                for color in colors:
                    color = color.strip()
                    count, color = color.split(' ')
                    min_[color] = max(min_[color], int(count))
            sum += min_['red'] * min_['green'] * min_['blue']
    return sum

print(solution('input.txt'))