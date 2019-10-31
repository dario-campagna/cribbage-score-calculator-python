from enum import Enum
from typing import List

class Suite(Enum):
    HEARTS = '♥'
    CLUBS = '♣'
    DIAMONDS = '♦'
    SPADES = '♠'


class Card(object):
    def __init__(self, rank: str, suite: Suite):
        super()
        self.rank = rank
        self.suite = suite

    def __eq__(self, value):
        return self.rank == value.rank and self.suite == value.suite


class CribbageHand(object):
    def __init__(self, cards: List[Card]):
        super()
        self.cards = cards

    def number_of_pairs(self):
        return self.__count_pairs__(self.cards[0], self.cards[1:])

    def __count_pairs__(self, card, other_cards):
        if len(other_cards) == 0:
            return 0
        else:
            return len([c for c in other_cards if c.rank == card.rank]) + self.__count_pairs__(other_cards[0], other_cards[1:])

    def __eq__(self, value):
        return self.cards == value.cards
