
cards = {}
# cards: {'card_1': 2}
# X [[card_1, 12], [card_2, 10]]

while True:
    card = input().lower()
    # TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
    # cards[card] = cards.get(card) + 1
                    # cards[card] + 1
    cards[card] = cards.get(card, 0) + 1

    if cards[card] == 6:
        print(f"{card}")
        break