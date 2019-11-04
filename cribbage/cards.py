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
    RANKS_DICT = {'A': (0, 1), '2': (1, 2), '3': (2, 3), '4': (3, 4),
                  '5': (4, 5), '6': (5, 6), '7': (6, 7), '8': (7, 8),
                  '9': (8, 9), '0': (9, 10), 'J': (10, 10), 'Q': (11, 10),
                  'K': (12, 10)}
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

    def int_value(self):
        return Rank.RANKS_DICT[self.value][1]

    def __eq__(self, that):
        if isinstance(that, Rank):
            return self.value == that.value
        else:
            return False

    def __lt__(self, that):
        this_pos_value = Rank.RANKS_DICT[self.value][0]
        that_pos_value = Rank.RANKS_DICT[that.value][0]
        return this_pos_value < that_pos_value


class Card(object):

    def __init__(self, rank: Rank, suite: Suite):
        super()
        self.rank = rank
        self.suite = suite

    def __eq__(self, that):
        if isinstance(that, Card):
            return self.rank == that.rank and self.suite == that.suite
        else:
            return False

    def __lt__(self, value):
        return self.rank < value.rank


class CribbageHand(object):
    def __init__(self, cards: List[Card]):
        super()
        self.hand_cards = cards[:-1]
        self.starter_card = cards[-1]

    def number_of_pairs(self):
        combs_of_two_cards = combinations(self.__all_cards_sorted__(), 2)
        return len([cards for cards in combs_of_two_cards
                    if cards[0].rank == cards[1].rank])

    def is_flush(self):
        return self.__count_same_suite__() == 3

    def holds_nob(self):
        return Card(Rank('J'), self.starter_card.suite) in self.hand_cards

    def is_run_of_five(self):
        return Rank.are_consecutives(self.__all_cards_ranks_sorted__())

    def is_run_of_four(self):
        return len(self.__runs_of__(4)) > 0

    def number_of_runs_of_three(self):
        return len(self.__runs_of__(3))

    def number_of_fifteen_twos(self):
        return sum(self.__totals_fifteen__(n) for n in range(2, 6))

    def __totals_fifteen__(self, n):
        combs_of_ranks = combinations(self.__all_cards_ranks_sorted__(), n)
        return len([ranks for ranks in combs_of_ranks
                    if sum(rank.int_value() for rank in ranks) == 15])

    def __runs_of__(self, n):
        combs_of_ranks = combinations(self.__all_cards_ranks_sorted__(), n)
        return [ranks for ranks in combs_of_ranks
                if Rank.are_consecutives(ranks)]

    def __count_same_suite__(self):
        return len([card for card in self.hand_cards[1:]
                    if card.suite == self.hand_cards[0].suite])

    def __all_cards_sorted__(self):
        return sorted(self.hand_cards + [self.starter_card])

    def __all_cards_ranks_sorted__(self):
        return [card.rank for card in self.__all_cards_sorted__()]

    def __eq__(self, value):
        return (self.hand_cards == value.hand_cards and
                self.starter_card == value.starter_card)
