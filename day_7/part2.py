card_types = {'A': 'a', 'K': 'b', 'Q': 'c', 'T': 'd', '9': 'e', '8': 'f', '7': 'g', '6': 'h', '5': 'i',
              '4': 'j', '3': 'k', '2': 'l', 'J': 'm'}

with open("input.txt") as f:
    hands = [{'cards': line.split()[0],
              'bid': int(line.split()[1]),
              'type': 0} for line in f.readlines()]

for hand in hands:
    for key in card_types.keys():
        # replace card names by their value in card_types to enable alphabetical sorting for determining rank
        hand['cards'] = hand['cards'].replace(key, card_types[key])
    # if all the cards in the hand are the same
    if len(set(hand['cards'])) == 1:
        hand['type'] = 1
    # if there are two different kinds of cards in the hand
    elif len(set(hand['cards'])) == 2:
        sorted_cards = sorted(hand['cards'])
        if sorted_cards[1] == sorted_cards[3]:
            if 'm' in hand['cards']:
                hand['type'] = 1
            else:
                hand['type'] = 2

        else:
            if 'm' in hand['cards']:
                hand['type'] = 1
            else:
                hand['type'] = 3
    # if there are three different kinds of cards in the hand
    elif len(set(hand['cards'])) == 3:
        for card in hand['cards']:
            if hand['cards'].count(card) == 3:
                if 'm' in hand['cards']:
                    hand['type'] = 2
                else:
                    hand['type'] = 4
                break

            if 'm' in hand['cards'] and hand['cards'].count('m') == 2:
                hand['type'] = 2
            elif 'm' in hand['cards'] and hand['cards'].count('m') == 1:
                hand['type'] = 3
            else:
                hand['type'] = 5

    # if there are four different kinds of cards in the hand
    elif len(set(hand['cards'])) == 4:
        if 'm' in hand['cards']:
            hand['type'] = 4
        else:
            hand['type'] = 6

    # if all the cards in the hand are different
    else:
        if 'm' in hand['cards']:
            hand['type'] = 6
        else:
            hand['type'] = 7

hands.sort(key=lambda x: x['cards'], reverse=True)
hands.sort(key=lambda x: x['type'], reverse=True)

result = 0
for i, hand in enumerate(hands):
    result += hand['bid'] * (i+1)

print(hands)
print(result)
