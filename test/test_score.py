import unittest

from production.cribbage.cards import CribbageHand, Card, Suite, Rank
from production.cribbage.score import score


class TestPairs(unittest.TestCase):
    def test_two_points_for_a_pair_of_cards_of_a_kind(self):
        cribbage_hand = CribbageHand([
            Card(Rank('2'), Suite.DIAMONDS),
            Card(Rank('A'), Suite.DIAMONDS),
            Card(Rank('2'), Suite.CLUBS),
            Card(Rank('7'), Suite.DIAMONDS),
            Card(Rank('9'), Suite.DIAMONDS),
        ])
        self.assertEqual(2, score(cribbage_hand))

    def test_four_points_for_two_pairs_of_cards_of_a_kind(self):
        cribbage_hand = CribbageHand([
            Card(Rank('3'), Suite.DIAMONDS),
            Card(Rank('A'), Suite.DIAMONDS),
            Card(Rank('3'), Suite.CLUBS),
            Card(Rank('7'), Suite.DIAMONDS),
            Card(Rank('A'), Suite.HEARTS),
        ])
        self.assertEqual(4, score(cribbage_hand))

    def test_six_points_for_three_cards_of_a_kind(self):
        cribbage_hand = CribbageHand([
            Card(Rank('6'), Suite.DIAMONDS),
            Card(Rank('A'), Suite.DIAMONDS),
            Card(Rank('6'), Suite.CLUBS),
            Card(Rank('7'), Suite.DIAMONDS),
            Card(Rank('6'), Suite.SPADES),
        ])
        self.assertEqual(6, score(cribbage_hand))

    def test_twelve_points_for_four_cards_of_a_kind(self):
        cribbage_hand = CribbageHand([
            Card(Rank('0'), Suite.DIAMONDS),
            Card(Rank('A'), Suite.DIAMONDS),
            Card(Rank('0'), Suite.CLUBS),
            Card(Rank('0'), Suite.HEARTS),
            Card(Rank('0'), Suite.SPADES),
        ])
        self.assertEqual(12, score(cribbage_hand))


class TestFlush(unittest.TestCase):
    def test_four_points_for_a_flush(self):
        cribbage_hand = CribbageHand([
            Card(Rank('3'), Suite.DIAMONDS),
            Card(Rank('A'), Suite.DIAMONDS),
            Card(Rank('7'), Suite.DIAMONDS),
            Card(Rank('9'), Suite.DIAMONDS),
            Card(Rank('J'), Suite.SPADES),
        ])
        self.assertEqual(4, score(cribbage_hand))

    def test_one_point_for_the_J_of_the_same_suite_as_the_starter_card(self):
        cribbage_hand = CribbageHand([
            Card(Rank('3'), Suite.DIAMONDS),
            Card(Rank('J'), Suite.SPADES),
            Card(Rank('7'), Suite.DIAMONDS),
            Card(Rank('9'), Suite.DIAMONDS),
            Card(Rank('A'), Suite.SPADES),
        ])
        self.assertEqual(1, score(cribbage_hand))


class TestRuns(unittest.TestCase):
    def test_five_points_for_run_of_five(self):
        cribbage_hand = CribbageHand([
            Card(Rank('9'), Suite.DIAMONDS),
            Card(Rank('0'), Suite.SPADES),
            Card(Rank('J'), Suite.DIAMONDS),
            Card(Rank('Q'), Suite.DIAMONDS),
            Card(Rank('K'), Suite.SPADES),
        ])
        self.assertEqual(5, score(cribbage_hand))

    def test_four_points_for_run_of_four(self):
        cribbage_hand = CribbageHand([
            Card(Rank('2'), Suite.DIAMONDS),
            Card(Rank('0'), Suite.SPADES),
            Card(Rank('J'), Suite.DIAMONDS),
            Card(Rank('Q'), Suite.DIAMONDS),
            Card(Rank('K'), Suite.SPADES),
        ])
        self.assertEqual(4, score(cribbage_hand))

    def test_three_points_for_a_run_of_three(self):
        cribbage_hand = CribbageHand([
            Card(Rank('8'), Suite.DIAMONDS),
            Card(Rank('A'), Suite.DIAMONDS),
            Card(Rank('5'), Suite.CLUBS),
            Card(Rank('7'), Suite.DIAMONDS),
            Card(Rank('9'), Suite.SPADES),
        ])
        self.assertEqual(3, score(cribbage_hand))
    
    def test_eight_points_for_double_run(self):
        cribbage_hand = CribbageHand([
            Card(Rank('2'), Suite.DIAMONDS),
            Card(Rank('2'), Suite.HEARTS),
            Card(Rank('3'), Suite.CLUBS),
            Card(Rank('7'), Suite.DIAMONDS),
            Card(Rank('4'), Suite.SPADES),
        ])
        self.assertEqual(8, score(cribbage_hand))
    
    def test_fiteen_points_for_triple_run(self):
        cribbage_hand = CribbageHand([
            Card(Rank('2'), Suite.DIAMONDS),
            Card(Rank('2'), Suite.HEARTS),
            Card(Rank('3'), Suite.CLUBS),
            Card(Rank('4'), Suite.DIAMONDS),
            Card(Rank('2'), Suite.SPADES),
        ])
        self.assertEqual(15, score(cribbage_hand))
    
    def test_sixteen_points_for_double_double_run(self):
        cribbage_hand = CribbageHand([
            Card(Rank('4'), Suite.DIAMONDS),
            Card(Rank('2'), Suite.HEARTS),
            Card(Rank('3'), Suite.CLUBS),
            Card(Rank('4'), Suite.DIAMONDS),
            Card(Rank('3'), Suite.SPADES),
        ])
        self.assertEqual(16, score(cribbage_hand))
