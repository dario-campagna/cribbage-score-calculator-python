import unittest
from production.cribbage.cards import Rank


class TestRank(unittest.TestCase):
    def test_consecutives(self):
        self.assertTrue(Rank.are_consecutives(
            [Rank('A'), Rank('2'), Rank('3')]))

    def test_not_consecutives(self):
        self.assertFalse(Rank.are_consecutives(
            [Rank('6'), Rank('6'), Rank('5')]))
