from enum import Enum
import re


def parse(cards_as_text):
    cards = [parse_card(card_as_text)
             for card_as_text in re.findall('.[♥♣♦♠]', cards_as_text)]
    return CribbageHand(cards)


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

    def __eq__(self, value):
        return self.rank == value.rank and self.suite == value.suite


class CribbageHand(object):
    def __init__(self, hand_cards):
        super()
        self.hand_cards = hand_cards

    def __eq__(self, value):
        return self.hand_cards == value.hand_cards
