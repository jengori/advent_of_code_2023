# this is exactly the same parsing of input that was done for the part 1 solution
with open("input.txt") as f:
    data = f.readlines()
    breakpoints = [i for i, x in enumerate(data) if x == "\n"]
    breakpoints.append(len(data))
    seeds = [int(x) for x in data[0].split(":")[1].strip().split()]
    map_titles = [data[i+1].strip()[:-1] for i in breakpoints[:-1]]
    maps = {data[breakpoints[i] + 1].strip()[:-1]: [[int(y) for y in x.strip().split(" ")]
                                                    for x in data[breakpoints[i] + 2: breakpoints[i + 1]]]
            for i in range(len(breakpoints) - 1)}

# create a list of seed groups -
# each item in the list is a list containing 2 values - the start and end number (inclusive) of the seeds in a

seed_groups = []
for i, seed in enumerate(seeds):
    if i % 2 == 0:
        seed_groups.append([seeds[i], seeds[i]+seeds[i+1]-1])


def get_mapping_groups(map_num) -> list:
    """Takes a map number (index in map_titles) and returns a list of mapping groups
    Each mapping group is a list containing the start and end number of an (inclusive)
    range of item values that will all follow the same mapping rule"""
    mapping_groups = []
    for i, item in enumerate(maps[map_titles[map_num]]):
        mapping_groups.append([maps[map_titles[map_num]][i][1],
                               maps[map_titles[map_num]][i][1] + maps[map_titles[map_num]][i][2] - 1])
    mapping_groups.sort()
    for i in range(len(mapping_groups) - 1):
        if mapping_groups[i][1] + 1 < mapping_groups[i + 1][0]:
            mapping_groups.insert(i + 1, [mapping_groups[i][1] + 1, mapping_groups[i + 1][0] - 1])

    if mapping_groups[0][0] != 0:
        mapping_groups.insert(0, [0, mapping_groups[0][0] - 1])
    mapping_groups.append([mapping_groups[-1][1], 9223372036854775807])
    return mapping_groups


def divide_item_groups(map_num, item_groups):
    """Takes a map number (index in map_titles) and an item_groups list
    (same format as seed_groups (line 15) and subdivides the item groups that it contains
    into subgroups that all follow the same mapping rule"""
    mapping_groups = get_mapping_groups(map_num)
    groups_divided = []
    for item_group in item_groups:
        while item_group[1] not in [group[1] for group in groups_divided]:

            for mapping_group in mapping_groups:
                if item_group[0] in range(mapping_group[0], mapping_group[1] + 1) and item_group[1] in range(
                        mapping_group[0], mapping_group[1] + 1):
                    groups_divided.append(item_group)
                elif item_group[0] in range(mapping_group[0], mapping_group[1] + 1):
                    groups_divided.append([item_group[0], mapping_group[1]])
                    item_group[0] = mapping_group[1] + 1

    return groups_divided


def mapping(map_num, item_groups):
    """Takes item_group (this will be seeds_groups), applies all mappings, and
    returns mapped groups (this will be ranges of locations)"""
    if map_num == len(map_titles):
        return item_groups

    else:

        mapped_groups = []
        item_groups_divided = divide_item_groups(map_num, item_groups)
        for group in item_groups_divided:
            mapped = False
            for line in maps[map_titles[map_num]]:
                source_start = line[1]
                destination_start = line[0]
                range_length = line[2]

                if group[0] in range(source_start, source_start+range_length):
                    mapped_group = \
                        [destination_start + (group[0]-source_start), destination_start + (group[1]-source_start)]
                    mapped_groups.append(mapped_group)
                    mapped = True

            if not mapped:
                mapped_groups.append([group[0], group[1]])

        return mapping(map_num+1, mapped_groups)


location_groups = mapping(0, seed_groups)
result = min([group[0] for group in location_groups])
print(result)
