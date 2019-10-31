import unittest

from production.cribbage.cards import Card, Suite


class TestCard(unittest.TestCase):
    def test_next_rank(self):
        self.assertEqual('3',
                         Card('2', Suite.DIAMONDS).__successor_rank__())
        self.assertEqual('K',
                         Card('K', Suite.DIAMONDS).__successor_rank__())

    def test_has_next_in(self):
        self.assertTrue(Card('A', Suite.CLUBS).has_next_in(
            [Card('3', Suite.DIAMONDS), Card('2', Suite.HEARTS)]))
        self.assertFalse(Card('A', Suite.CLUBS).has_next_in(
            [Card('3', Suite.DIAMONDS), Card('K', Suite.HEARTS)]))
