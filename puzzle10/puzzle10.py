def process_blocks(input_file):
    with open(input_file) as file:
        inputs, *blocks = file.read().split("\n\n")

    seeds = [
        (start, start + interval)
        for start, interval in zip(*[iter(map(int, inputs.split(":")[1].split()))] * 2)
    ]

    for block in blocks:
        ranges = [list(map(int, line.split())) for line in block.splitlines()[1:]]
        new_seeds = []

        while seeds:
            s, e = seeds.pop()
            for a, b, c in ranges:
                overlap_start = max(s, b)
                overlap_end = min(e, b + c)
                if overlap_start < overlap_end:
                    new_seeds.append((overlap_start - b + a, overlap_end - b + a))
                    if overlap_start > s:
                        seeds.append((s, overlap_start))
                    if e > overlap_end:
                        seeds.append((overlap_end, e))
                    break
            else:
                new_seeds.append((s, e))
        seeds = new_seeds

    return min(seeds)[0]


print(process_blocks("input.txt"))
