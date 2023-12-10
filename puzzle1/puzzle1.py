def solution(file):
    def first_and_last_digit(s):
        first_digit = next((int(c) for c in s if c.isdigit()), 0)
        last_digit = next((int(c) for c in reversed(s) if c.isdigit()), 0)
        return first_digit, last_digit

    with open(file, 'r') as f:
        return sum(first * 10 + last for line in f for first, last in [first_and_last_digit(line)])

print(solution('input.txt'))