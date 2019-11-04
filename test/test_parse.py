import unittest

from cribbage.parse import parse_hand, parse_card
from cribbage.cards import Suite, Card, CribbageHand, Rank


class TestParseCard(unittest.TestCase):
    def test_parse_rank_5(self):
        card = parse_card('5♥')
        self.assertEqual(Rank('5'), card.rank)

    def test_parse_rank_A(self):
        card = parse_card('A♥')
        self.assertEqual(Rank('A'), card.rank)

    def test_parse_suite_hearts(self):
        card = parse_card('0♥')
        self.assertEqual(Suite.HEARTS, card.suite)

    def test_parse_suite_clubs(self):
        card = parse_card('0♣︎')
        self.assertEqual(Suite.CLUBS, card.suite)

    def test_parse_suite_diamonds(self):
        card = parse_card('0♦')
        self.assertEqual(Suite.DIAMONDS, card.suite)

    def test_parse_suite_spades(self):
        card = parse_card('0♠')
        self.assertEqual(Suite.SPADES, card.suite)


class TestParseCribbageHand(unittest.TestCase):
    def test_parse_two_cards(self):
        expected = CribbageHand(
            [Card(Rank('6'), Suite.SPADES), Card(Rank('8'), Suite.DIAMONDS)]
        )
        cribbage_hand = parse_hand('6♠8♦')
        self.assertEqual(expected, cribbage_hand)

    def test_parse_five_cards(self):
        expected = CribbageHand([
            Card(Rank('6'), Suite.SPADES),
            Card(Rank('8'), Suite.DIAMONDS),
            Card(Rank('A'), Suite.DIAMONDS),
            Card(Rank('3'), Suite.SPADES),
            Card(Rank('J'), Suite.SPADES)
        ])
        cribbage_hand = parse_hand('6♠8♦A♦3♠J♠')
        self.assertEqual(expected, cribbage_hand)
