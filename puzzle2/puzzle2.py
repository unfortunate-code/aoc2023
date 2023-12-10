import re


def solution(file):
    numbers = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
    }

    def first_and_last_digit(s):
        first = min(
            [(s.index(number), numbers[number]) for number in numbers if number in s]
        )[1]
        last = max(
            [(s.rindex(number), numbers[number]) for number in numbers if number in s]
        )[1]
        return first, last

    with open(file, "r") as f:
        return sum(
            first * 10 + last
            for line in f
            for first, last in [first_and_last_digit(line)]
        )


print(solution("input.txt"))
