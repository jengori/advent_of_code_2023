def get_winning_nums_list(s):
    return [int(char) for char in s.split(":")[1].split("|")[0].strip().split(" ") if char != ""]


def get_my_nums_list(s):
    return [int(char) for char in s.split(":")[1].split("|")[1].strip().split(" ") if char != ""]


def count_winning_nums(my_nums, winning_nums):
    return len([num for num in my_nums if num in winning_nums])


def calculate_score(winning_nums_count):
    if winning_nums_count == 0:
        return 0
    elif winning_nums_count == 1:
        return 1
    else:
        return 2 * calculate_score(winning_nums_count-1)


def total_score(file):
    total = 0
    with open(file) as f:
        for line in f:
            winning_numbers = get_winning_nums_list(line)
            my_numbers = get_my_nums_list(line)
            total += calculate_score(count_winning_nums(my_numbers, winning_numbers))
    return total


def max_card_num(file):
    with open(file) as f:
        return len(f.readlines())


def total_cards(file):
    max_card_number = max_card_num(file)
    cards_dict = {i + 1: 1 for i in range(max_card_number)}
    card_num = 1

    with open(file) as f:
        for line in f:
            winning_numbers_count = count_winning_nums(get_my_nums_list(line), get_winning_nums_list(line))
            for n in range(card_num + 1, min(card_num + 1 + winning_numbers_count, max_card_number + 1)):
                cards_dict[n] += cards_dict[card_num]
            card_num += 1

    return sum(cards_dict.values())


# Part 1 answer
print(total_score("input.txt"))
# Part 2 answer
print(total_cards("input.txt"))
