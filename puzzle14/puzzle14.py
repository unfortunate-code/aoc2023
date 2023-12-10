from collections import Counter


def solution(file):
    with open(file, "r") as f:
        lines = f.readlines()

    bids = []
    hands = []

    def score(hand):
        def type(hand):
            count = Counter(hand)
            j = count.pop("J", 0)
            max_v = 0
            max_k = ""
            for k, v in count.items():
                if v > max_v:
                    max_v = v
                    max_k = k
            count[max_k] += j
            if len(count) == 1:
                return 7
            elif len(count) == 2:
                if 2 in count.values():
                    return 5
                else:
                    return 6
            elif len(count) == 3:
                if 3 in count.values():
                    return 4
                else:
                    return 3
            elif len(count) == 4:
                return 2
            else:
                return 1

        def index(card):
            return "J23456789TJQKA".index(card)

        return (type(hand), *map(index, hand))

    for line in lines:
        hand, bid = line.split()
        bids.append(int(bid))
        hands.append((hand, len(hands)))
    hands.sort(key=lambda x: score(x[0]))
    res = 0
    for i, (hand, idx) in enumerate(hands):
        res += (i + 1) * bids[idx]
    return res


print(solution("input.txt"))
