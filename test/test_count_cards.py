import unittest

from production.cribbage.cards import CribbageHand, Card, Suite

class TestCountPairs(unittest.TestCase):
    def test_count_one_pair(self):
        cribbage_hand = CribbageHand([
            Card('2', Suite.DIAMONDS),
            Card('A', Suite.DIAMONDS),
            Card('2', Suite.CLUBS),
            Card('7', Suite.DIAMONDS),
            Card('9', Suite.DIAMONDS),
        ])
        self.assertEqual(1, cribbage_hand.number_of_pairs())

    def test_count_two_pairs(self):
        cribbage_hand = CribbageHand([
            Card('3', Suite.DIAMONDS),
            Card('A', Suite.DIAMONDS),
            Card('3', Suite.CLUBS),
            Card('7', Suite.DIAMONDS),
            Card('A', Suite.SPADES),
        ])
        self.assertEqual(2, cribbage_hand.number_of_pairs())

    def test_count_three_pairs(self):
        cribbage_hand = CribbageHand([
            Card('6', Suite.DIAMONDS),
            Card('A', Suite.DIAMONDS),
            Card('6', Suite.CLUBS),
            Card('7', Suite.DIAMONDS),
            Card('6', Suite.SPADES),
        ])
        self.assertEqual(3, cribbage_hand.number_of_pairs())

    def test_count_four_pairs(self):
        cribbage_hand = CribbageHand([
            Card('0', Suite.DIAMONDS),
            Card('A', Suite.DIAMONDS),
            Card('0', Suite.CLUBS),
            Card('0', Suite.HEARTS),
            Card('0', Suite.SPADES),
        ])
        self.assertEqual(6, cribbage_hand.number_of_pairs())
