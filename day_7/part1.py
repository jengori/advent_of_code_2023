card_types = {'A': 'a', 'K': 'b', 'Q': 'c', 'J': 'd', 'T': 'e', '9': 'f', '8': 'g', '7': 'h', '6': 'i', '5': 'j',
              '4': 'k', '3': 'l', '2': 'm'}

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
            hand['type'] = 2

        else:
            hand['type'] = 3

    # if there are three different kinds of cards in the hand
    elif len(set(hand['cards'])) == 3:
        for card in hand['cards']:
            if hand['cards'].count(card) == 3:
                hand['type'] = 4
                break
            hand['type'] = 5

    # if there are four different kinds of cards in the hand
    elif len(set(hand['cards'])) == 4:
        hand['type'] = 6

    # if all the cards in the hand are different
    else:
        hand['type'] = 7

hands.sort(key=lambda x: x['cards'], reverse=True)
hands.sort(key=lambda x: x['type'], reverse=True)

result = 0
for i, hand in enumerate(hands):
    result += hand['bid'] * (i+1)

print(result)



