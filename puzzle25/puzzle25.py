def solution(file):
    with open(file) as f:
        inputs = f.read().split("\n\n")

    # Finds palindrome that starts at the beginning or end and returns the largest of those.
    def find_palindrome(arr):
        res = -1
        loc = -1
        for j in range(len(arr) - 1, -1, -1):
            if j % 2 == 0:
                continue
            for k in range(j // 2 + 1):
                if arr[k] != arr[j - k]:
                    break
            else:
                res = j + 1
                loc = j // 2
                break
        for i in range(len(arr)):
            if (len(arr) - i - 1) % 2 == 0:
                continue
            for k in range((len(arr) - i + 1) // 2):
                if arr[i + k] != arr[len(arr) - k - 1]:
                    break
            else:
                if i > res:
                    res = len(arr) - i
                    loc = (len(arr) + i) // 2 - 1
                    break
        return res, loc

    # Maps the columns to integers for easy palindrome finding.
    def vertical_map(input):
        lines = input.split("\n")
        cols = zip(*lines)
        d = {}
        vert = []
        k = 0
        for col in cols:
            if col in d:
                vert.append(d[col])
            else:
                d[col] = k
                vert.append(k)
                k += 1
        return vert

    # Maps horizontal lines to integers for easy palindrome finding.
    def horizontal_map(input):
        lines = input.split("\n")
        d = {}
        hor = []
        k = 0
        for line in lines:
            if line in d:
                hor.append(d[line])
            else:
                d[line] = k
                hor.append(k)
                k += 1
        return hor

    sum = 0
    for input in inputs:
        # Find mirrors on both axes and take the largest.
        vert = vertical_map(input)
        hor = horizontal_map(input)
        res1, loc1 = find_palindrome(vert)
        res2, loc2 = find_palindrome(hor)
        if res1 > res2:
            # 1 indexed.
            sum += loc1 + 1
        else:
            # 1 indexed.
            sum += (loc2 + 1) * 100
    return sum


print(solution("input.txt"))
