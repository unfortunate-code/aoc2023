def solution(file_path, red, green, blue):
    counts = {'red': red, 'green': green, 'blue': blue}

    with open(file_path, 'r') as file:
        lines = file.readlines()

        sum_ids = 0
        for line in lines:
            game, draw_info = line.split(':')
            game_id = int(game.split()[1])
            draws = [draw.strip().split(',') for draw in draw_info.split(';')]

            if all(all(counts[color] >= int(count) for count, color in (item.split() for item in draw)) for draw in draws):
                sum_ids += game_id

        return sum_ids

print(solution('input.txt', 12, 13, 14))
