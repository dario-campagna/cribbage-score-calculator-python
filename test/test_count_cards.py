import unittest

from cribbage.cards import CribbageHand, Card, Suite, Rank


class TestCountPairs(unittest.TestCase):
    def test_count_one_pair(self):
        cribbage_hand = CribbageHand([
            Card(Rank('2'), Suite.DIAMONDS),
            Card(Rank('A'), Suite.DIAMONDS),
            Card(Rank('2'), Suite.CLUBS),
            Card(Rank('7'), Suite.DIAMONDS),
            Card(Rank('9'), Suite.DIAMONDS),
        ])
        self.assertEqual(1, cribbage_hand.number_of_pairs())

    def test_count_two_pairs(self):
        cribbage_hand = CribbageHand([
            Card(Rank('3'), Suite.DIAMONDS),
            Card(Rank('A'), Suite.DIAMONDS),
            Card(Rank('3'), Suite.CLUBS),
            Card(Rank('7'), Suite.DIAMONDS),
            Card(Rank('A'), Suite.SPADES),
        ])
        self.assertEqual(2, cribbage_hand.number_of_pairs())

    def test_count_three_pairs(self):
        cribbage_hand = CribbageHand([
            Card(Rank('6'), Suite.DIAMONDS),
            Card(Rank('A'), Suite.DIAMONDS),
            Card(Rank('6'), Suite.CLUBS),
            Card(Rank('7'), Suite.DIAMONDS),
            Card(Rank('6'), Suite.SPADES),
        ])
        self.assertEqual(3, cribbage_hand.number_of_pairs())

    def test_count_four_pairs(self):
        cribbage_hand = CribbageHand([
            Card(Rank('0'), Suite.DIAMONDS),
            Card(Rank('A'), Suite.DIAMONDS),
            Card(Rank('0'), Suite.CLUBS),
            Card(Rank('0'), Suite.HEARTS),
            Card(Rank('0'), Suite.SPADES),
        ])
        self.assertEqual(6, cribbage_hand.number_of_pairs())


class TestCountRuns(unittest.TestCase):
    def test_run_of_five(self):
        cribbage_hand = CribbageHand([
            Card(Rank('3'), Suite.DIAMONDS),
            Card(Rank('4'), Suite.DIAMONDS),
            Card(Rank('5'), Suite.CLUBS),
            Card(Rank('6'), Suite.HEARTS),
            Card(Rank('7'), Suite.SPADES),
        ])
        self.assertTrue(cribbage_hand.is_run_of_five())

    def test_not_run_of_five(self):
        cribbage_hand = CribbageHand([
            Card(Rank('3'), Suite.DIAMONDS),
            Card(Rank('4'), Suite.DIAMONDS),
            Card(Rank('J'), Suite.CLUBS),
            Card(Rank('K'), Suite.HEARTS),
            Card(Rank('A'), Suite.SPADES),
        ])
        self.assertFalse(cribbage_hand.is_run_of_five())

    def test_run_of_four(self):
        cribbage_hand = CribbageHand([
            Card(Rank('A'), Suite.DIAMONDS),
            Card(Rank('4'), Suite.DIAMONDS),
            Card(Rank('5'), Suite.CLUBS),
            Card(Rank('6'), Suite.HEARTS),
            Card(Rank('7'), Suite.SPADES),
        ])
        self.assertTrue(cribbage_hand.is_run_of_four())

    def test_not_run_of_four(self):
        cribbage_hand = CribbageHand([
            Card(Rank('6'), Suite.DIAMONDS),
            Card(Rank('A'), Suite.DIAMONDS),
            Card(Rank('6'), Suite.CLUBS),
            Card(Rank('7'), Suite.DIAMONDS),
            Card(Rank('6'), Suite.SPADES),
        ])
        self.assertFalse(cribbage_hand.is_run_of_four())

    def test_one_run_of_three(self):
        cribbage_hand = CribbageHand([
            Card(Rank('8'), Suite.DIAMONDS),
            Card(Rank('A'), Suite.DIAMONDS),
            Card(Rank('5'), Suite.CLUBS),
            Card(Rank('7'), Suite.DIAMONDS),
            Card(Rank('9'), Suite.SPADES),
        ])
        self.assertEqual(1, cribbage_hand.number_of_runs_of_three())
    
    def test_two_runs_of_three(self):
        cribbage_hand = CribbageHand([
            Card(Rank('2'), Suite.DIAMONDS),
            Card(Rank('2'), Suite.HEARTS),
            Card(Rank('3'), Suite.CLUBS),
            Card(Rank('7'), Suite.DIAMONDS),
            Card(Rank('4'), Suite.SPADES),
        ])
        self.assertEqual(2, cribbage_hand.number_of_runs_of_three())
