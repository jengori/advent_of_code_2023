with open("example_input.txt") as f:
    data = f.readlines()
    breakpoints = [i for i, x in enumerate(data) if x == "\n"]
    breakpoints.append(len(data))
    seeds = [int(x) for x in data[0].split(":")[1].strip().split()]
    map_titles = [data[i+1].strip()[:-1] for i in breakpoints[:-1]]
    maps = \
        {data[breakpoints[i] + 1].strip()[:-1]: [[int(y) for y in x.strip().split(" ")]
                                                 for x in data[breakpoints[i] + 2: breakpoints[i + 1]]]
         for i in range(len(breakpoints) - 1)}


def mapping(map_num, source_num):
    if map_num == len(map_titles):
        return source_num
    else:
        for line in maps[map_titles[map_num]]:
            source_start = line[1]
            destination_start = line[0]
            range_length = line[2]

            if source_num in range(source_start, source_start+range_length):
                item_number = destination_start + (source_num-source_start)
                return mapping(map_num+1, item_number)

        return mapping(map_num+1, source_num)


part_1_answer = min([mapping(0, seed) for seed in seeds])
print(part_1_answer)
