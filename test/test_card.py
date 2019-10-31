import unittest

from production.cribbage.cards import Card, Suite


class TestCard(unittest.TestCase):
    def test_next(self):
        self.assertEqual(Card('3', Suite.DIAMONDS),
                         Card('2', Suite.DIAMONDS).next())
        self.assertEqual(Card('K', Suite.DIAMONDS),
                         Card('K', Suite.DIAMONDS).next())
