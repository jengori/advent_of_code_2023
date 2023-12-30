result = 0

with open("input.txt") as f:
    data = [line.strip() for line in f.readlines()]

for line in data:
    criteria = line.split(" ")[0]
    spring_groups = [int(x) for x in line.split(" ")[1].split(",")]

    possible_start_indices_all_groups = []

    for i, group in enumerate(spring_groups):
        possible_start_indices = []

        spaces_needed_for_previous_groups = sum(spring_groups[:i]) + len(spring_groups[:i])
        spaces_needed_for_subsequent_groups = sum(spring_groups[i+1:]) + len(spring_groups[i+1:])

        for n in range(len(criteria)):
            if spaces_needed_for_previous_groups <= n <= len(criteria) - spaces_needed_for_subsequent_groups - group\
                    and '.' not in criteria[n:n+group]:

                possible_start_indices.append(n)

        possible_start_indices_all_groups.append(possible_start_indices)

    poss_positions = []

    if len(possible_start_indices_all_groups) == 2:
        for x in possible_start_indices_all_groups[0]:
            for y in possible_start_indices_all_groups[1]:
                if x + spring_groups[0] < y:
                    occupied_indices = []
                    for n in range(x, x+spring_groups[0]):
                        occupied_indices.append(n)
                    for m in range(y, y+spring_groups[1]):
                        occupied_indices.append(m)

                    unoccupied_indices = set([num for num in range(len(criteria))]) - set(occupied_indices)
                    ignore = False
                    for i in unoccupied_indices:
                        if criteria[i] == "#":
                            ignore = True
                    if not ignore:
                        poss_positions.append([x, y])

    elif len(possible_start_indices_all_groups) == 3:
        for x in possible_start_indices_all_groups[0]:
            for y in possible_start_indices_all_groups[1]:
                for z in possible_start_indices_all_groups[2]:
                    if x + spring_groups[0] < y and y + spring_groups[1] < z:
                        occupied_indices = []
                        for n in range(x, x + spring_groups[0]):
                            occupied_indices.append(n)
                        for m in range(y, y + spring_groups[1]):
                            occupied_indices.append(m)
                        for p in range(z, z + spring_groups[2]):
                            occupied_indices.append(p)

                        unoccupied_indices = set([num for num in range(len(criteria))]) - set(occupied_indices)
                        ignore = False
                        for i in unoccupied_indices:
                            if criteria[i] == "#":
                                ignore = True
                        if not ignore:
                            poss_positions.append([x, y, z])

    elif len(possible_start_indices_all_groups) == 4:
        for x in possible_start_indices_all_groups[0]:
            for y in possible_start_indices_all_groups[1]:
                for z in possible_start_indices_all_groups[2]:
                    for v in possible_start_indices_all_groups[3]:
                        if x + spring_groups[0] < y and \
                                y + spring_groups[1] < z and \
                                z + spring_groups[2] < v:
                            occupied_indices = []
                            for n in range(x, x + spring_groups[0]):
                                occupied_indices.append(n)
                            for m in range(y, y + spring_groups[1]):
                                occupied_indices.append(m)
                            for p in range(z, z + spring_groups[2]):
                                occupied_indices.append(p)
                            for q in range(v, v + spring_groups[3]):
                                occupied_indices.append(q)
                            unoccupied_indices = set([num for num in range(len(criteria))]) - set(occupied_indices)
                            ignore = False
                            for i in unoccupied_indices:
                                if criteria[i] == "#":
                                    ignore = True
                            if not ignore:
                                poss_positions.append([x, y, z, v])

    elif len(possible_start_indices_all_groups) == 5:
        for x in possible_start_indices_all_groups[0]:
            for y in possible_start_indices_all_groups[1]:
                for z in possible_start_indices_all_groups[2]:
                    for v in possible_start_indices_all_groups[3]:
                        for w in possible_start_indices_all_groups[4]:
                            if x + spring_groups[0] < y and \
                                    y + spring_groups[1] < z and \
                                    z + spring_groups[2] < v and \
                                    v + spring_groups[3] < w:
                                occupied_indices = []
                                for n in range(x, x + spring_groups[0]):
                                    occupied_indices.append(n)
                                for m in range(y, y + spring_groups[1]):
                                    occupied_indices.append(m)
                                for p in range(z, z + spring_groups[2]):
                                    occupied_indices.append(p)
                                for q in range(v, v + spring_groups[3]):
                                    occupied_indices.append(q)
                                for r in range(w, w + spring_groups[4]):
                                    occupied_indices.append(r)

                                unoccupied_indices = set([num for num in range(len(criteria))])-set(occupied_indices)
                                ignore = False
                                for i in unoccupied_indices:
                                    if criteria[i] == "#":
                                        ignore = True
                                if not ignore:
                                    poss_positions.append([x, y, z, v, w])

    elif len(possible_start_indices_all_groups) == 6:
        for x in possible_start_indices_all_groups[0]:
            for y in possible_start_indices_all_groups[1]:
                for z in possible_start_indices_all_groups[2]:
                    for v in possible_start_indices_all_groups[3]:
                        for w in possible_start_indices_all_groups[4]:
                            for u in possible_start_indices_all_groups[5]:
                                if x + spring_groups[0] < y and \
                                        y + spring_groups[1] < z and \
                                        z + spring_groups[2] < v and \
                                        v + spring_groups[3] < w and \
                                        w + spring_groups[4] < u:
                                    occupied_indices = []
                                    for n in range(x, x + spring_groups[0]):
                                        occupied_indices.append(n)
                                    for m in range(y, y + spring_groups[1]):
                                        occupied_indices.append(m)
                                    for p in range(z, z + spring_groups[2]):
                                        occupied_indices.append(p)
                                    for q in range(v, v + spring_groups[3]):
                                        occupied_indices.append(q)
                                    for r in range(w, w + spring_groups[4]):
                                        occupied_indices.append(r)
                                    for s in range(u, u + spring_groups[5]):
                                        occupied_indices.append(s)

                                    unoccupied_indices = set([num for num in range(len(criteria))])-set(occupied_indices)
                                    ignore = False
                                    for i in unoccupied_indices:
                                        if criteria[i] == "#":
                                            ignore = True
                                    if not ignore:
                                        poss_positions.append([x, y, z, v, w, u])

    result += len(poss_positions)
print(result)




