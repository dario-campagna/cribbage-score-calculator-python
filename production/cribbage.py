from enum import Enum


def parse_card(card_as_text):
    return Card(card_as_text[0], Suite(card_as_text[1]))


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
