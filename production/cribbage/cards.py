from enum import Enum

class Suite(Enum):
    HEARTS = '♥'
    CLUBS = '♣'
    DIAMONDS = '♦'
    SPADES = '♠'


class Card(object):
    def __init__(self, rank, suite):
        super()
        self.rank = rank
        self.suite = suite

    def __eq__(self, value):
        return self.rank == value.rank and self.suite == value.suite


class CribbageHand(object):
    def __init__(self, hand_cards):
        super()
        self.hand_cards = hand_cards

    def __eq__(self, value):
        return self.hand_cards == value.hand_cards
