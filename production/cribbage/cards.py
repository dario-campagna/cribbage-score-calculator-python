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
        self.ranks = ('A', '2', '3', '4', '5', '6',
                      '7', '8', '9', '0', 'J', 'Q', 'K')
        self.rank = rank
        self.suite = suite

    def next(self):
        if (self.rank == 'K'):
            return self
        else:
            next_rank = self.ranks[self.ranks.index(self.rank) + 1]
            return Card(next_rank, self.suite)

    def has_next_in(self, cards):
        successors = [card for card in cards if card.rank == self.next().rank]
        return len(successors) > 0

    def __eq__(self, value):
        return self.rank == value.rank and self.suite == value.suite

    def __lt__(self, value):
        return self.ranks.index(self.rank) < self.ranks.index(value.rank)


class CribbageHand(object):
    def __init__(self, cards: List[Card]):
        super()
        self.hand_cards = cards[:-1]
        self.starter_card = cards[-1]

    def number_of_pairs(self):
        return self.__count_pairs__(self.starter_card, self.hand_cards)

    def is_flush(self):
        return self.__count_same_suite__() == 3

    def holds_nob(self):
        return Card('J', self.starter_card.suite) in self.hand_cards

    def is_run_of_five(self):
        all_cards = self.hand_cards[:] + [self.starter_card]
        return self.__check_consecutives__(sorted(all_cards))

    def __check_consecutives__(self, cards):
        return all(card.has_next_in(cards) for card in cards[:-1])

    def __count_same_suite__(self):
        return len([c for c in self.hand_cards[1:]
                    if c.suite == self.hand_cards[0].suite])

    def __count_pairs__(self, card, other_cards):
        if len(other_cards) == 0:
            return 0
        else:
            return (len([c for c in other_cards if c.rank == card.rank]) +
                    self.__count_pairs__(other_cards[0], other_cards[1:]))

    def __eq__(self, value):
        return (self.hand_cards == value.hand_cards and
                self.starter_card == value.starter_card)
