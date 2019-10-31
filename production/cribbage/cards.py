import re
from itertools import combinations
from enum import Enum
from typing import List


class Suite(Enum):
    HEARTS = '♥'
    CLUBS = '♣'
    DIAMONDS = '♦'
    SPADES = '♠'


class Rank(object):
    RANKS_DICT = {'A': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5,
                  '7': 6, '8': 7, '9': 8, '0': 9, 'J': 10, 'Q': 11, 'K': 12}
    RANKS_AS_STRINGS = ''.join(RANKS_DICT.keys())

    def __init__(self, value: str):
        super()
        self.value = value

    @staticmethod
    def are_consecutives(ranks):
        ranks = ''.join(rank.value for rank in ranks)
        if re.search(ranks, Rank.RANKS_AS_STRINGS):
            return True
        else:
            return False

    def __eq__(self, value):
        return self.value == value

    def __lt__(self, that):
        this_pos_value = Rank.RANKS_DICT[self.value]
        that_pos_value = Rank.RANKS_DICT[that.value]
        return this_pos_value < that_pos_value


class Card(object):

    def __init__(self, rank: Rank, suite: Suite):
        super()
        self.rank = rank
        self.suite = suite

    def __eq__(self, value):
        return self.rank == value.rank and self.suite == value.suite

    def __lt__(self, value):
        return self.rank < value.rank


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
        return Rank.are_consecutives(self.__all_cards_ranks_sorted__())

    def is_run_of_four(self):
        tuples = combinations(self.__all_cards_ranks_sorted__(), 4)
        runs = [t for t in tuples if Rank.are_consecutives(t)]
        return len(runs) == 1

    def __count_same_suite__(self):
        return len([c for c in self.hand_cards[1:]
                    if c.suite == self.hand_cards[0].suite])

    def __all_cards_sorted__(self):
        return sorted(self.hand_cards + [self.starter_card])

    def __all_cards_ranks_sorted__(self):
        return [card.rank for card in self.__all_cards_sorted__()]

    def __eq__(self, value):
        return (self.hand_cards == value.hand_cards and
                self.starter_card == value.starter_card)
