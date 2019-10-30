import unittest

from production.cribbage import parse_card, Suite


class TestParseCard(unittest.TestCase):
    def test_parse_rank_5(self):
        card = parse_card('5♥')
        self.assertEqual('5', card.rank)

    def test_parse_rank_A(self):
        card = parse_card('A♥')
        self.assertEqual('A', card.rank)

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
