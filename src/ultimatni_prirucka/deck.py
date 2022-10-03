from collections import namedtuple


Card = namedtuple("Card", ["colour", "value"])


class Deck:
    values = [str(n) for n in range(2, 11)] + list('JQKA')
    colours = ['diamond', 'spade', 'club', 'heart']

    def __init__(self):
        self._cards = [
            Card(colour, value)
            for colour in Deck.colours
            for value in Deck.values
        ]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]