import re
from itertools import combinations
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

    def has_next_in(self, cards):
        successors = [c for c in cards if c.rank == self.__successor_rank__()]
        return len(successors) > 0

    def __successor_rank__(self):
        if (self.rank == 'K'):
            return self.rank
        else:
            return self.ranks[self.ranks.index(self.rank) + 1]

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
        tuples = combinations(self.__all_cards_sorted__(), 2)
        return len([t for t in tuples if t[0].rank == t[1].rank])

    def is_flush(self):
        return self.__count_same_suite__() == 3

    def holds_nob(self):
        return Card('J', self.starter_card.suite) in self.hand_cards

    def is_run_of_five(self):
        all_cards = self.__all_cards_sorted__()
        return self.__are_consecutives__(all_cards)

    def is_run_of_four(self):
        tuples = combinations(self.__all_cards_sorted__(), 4)
        runs = [t for t in tuples if self.__are_consecutives__(t)]
        return len(runs) == 1

    def __are_consecutives__(self, cards):
        ranks = ('A', '2', '3', '4', '5', '6',
                      '7', '8', '9', '0', 'J', 'Q', 'K')
        card_ranks = ''.join(card.rank for card in cards)
        if re.search(card_ranks, ''.join(ranks)):
            return True
        else:
            return False

    def __count_same_suite__(self):
        return len([c for c in self.hand_cards[1:]
                    if c.suite == self.hand_cards[0].suite])

    def __all_cards_sorted__(self):
        return sorted(self.hand_cards + [self.starter_card])

    def __eq__(self, value):
        return (self.hand_cards == value.hand_cards and
                self.starter_card == value.starter_card)
