import unittest

from production.cribbage import parse_card

class TestParse(unittest.TestCase):
    def test_parse_rank_5(self):
        card = parse_card('5♥️')
        self.assertEqual(5, card.rank)