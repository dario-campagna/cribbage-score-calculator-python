import re
from production.cribbage.cards import CribbageHand, Card, Suite


def parse_hand(cards_as_text: str):
    cards = [parse_card(card_as_text)
             for card_as_text in re.findall('.[♥♣♦♠]', cards_as_text)]
    return CribbageHand(cards)


def parse_card(card_as_text: str):
    return Card(card_as_text[0], Suite(card_as_text[1]))
