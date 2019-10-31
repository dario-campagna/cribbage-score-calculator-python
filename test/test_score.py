import unittest

from production.cribbage.cards import CribbageHand, Card, Suite
from production.cribbage.score import score


class TestPairs(unittest.TestCase):
    def test_two_points_for_a_pair_of_cards_of_a_kind(self):
        cribbage_hand = CribbageHand([
            Card('2', Suite.DIAMONDS),
            Card('A', Suite.DIAMONDS),
            Card('2', Suite.CLUBS),
            Card('7', Suite.DIAMONDS),
            Card('9', Suite.DIAMONDS),
        ])
        self.assertEqual(2, score(cribbage_hand))

    def test_four_points_for_two_pairs_of_cards_of_a_kind(self):
        cribbage_hand = CribbageHand([
            Card('3', Suite.DIAMONDS),
            Card('A', Suite.DIAMONDS),
            Card('3', Suite.CLUBS),
            Card('7', Suite.DIAMONDS),
            Card('A', Suite.HEARTS),
        ])
        self.assertEqual(4, score(cribbage_hand))

    def test_six_points_for_three_cards_of_a_kind(self):
        cribbage_hand = CribbageHand([
            Card('6', Suite.DIAMONDS),
            Card('A', Suite.DIAMONDS),
            Card('6', Suite.CLUBS),
            Card('7', Suite.DIAMONDS),
            Card('6', Suite.SPADES),
        ])
        self.assertEqual(6, score(cribbage_hand))

    def test_twelve_points_for_four_cards_of_a_kind(self):
        cribbage_hand = CribbageHand([
            Card('0', Suite.DIAMONDS),
            Card('A', Suite.DIAMONDS),
            Card('0', Suite.CLUBS),
            Card('0', Suite.HEARTS),
            Card('0', Suite.SPADES),
        ])
        self.assertEqual(12, score(cribbage_hand))


class TestFlush(unittest.TestCase):
    def test_four_points_for_a_flush(self):
        cribbage_hand = CribbageHand([
            Card('3', Suite.DIAMONDS),
            Card('A', Suite.DIAMONDS),
            Card('7', Suite.DIAMONDS),
            Card('9', Suite.DIAMONDS),
            Card('J', Suite.SPADES),
        ])
        self.assertEqual(4, score(cribbage_hand))

    def test_one_point_for_the_J_of_the_same_suite_as_the_starter_card(self):
        cribbage_hand = CribbageHand([
            Card('3', Suite.DIAMONDS),
            Card('J', Suite.SPADES),
            Card('7', Suite.DIAMONDS),
            Card('9', Suite.DIAMONDS),
            Card('0', Suite.SPADES),
        ])
        self.assertEqual(1, score(cribbage_hand))
