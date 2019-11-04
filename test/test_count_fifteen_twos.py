import unittest
from production.cribbage.cards import CribbageHand, Suite, Rank, Card


class TestFifteenTwos(unittest.TestCase):
    def test_two_cards(self):
        cribbage_hand = CribbageHand([
            Card(Rank('0'), Suite.CLUBS),
            Card(Rank('2'), Suite.CLUBS),
            Card(Rank('5'), Suite.CLUBS),
            Card(Rank('9'), Suite.DIAMONDS),
            Card(Rank('9'), Suite.CLUBS)
        ])
        self.assertEqual(1, cribbage_hand.number_of_fifteen_twos())
        cribbage_hand = CribbageHand([
            Card(Rank('0'), Suite.CLUBS),
            Card(Rank('2'), Suite.CLUBS),
            Card(Rank('5'), Suite.CLUBS),
            Card(Rank('9'), Suite.DIAMONDS),
            Card(Rank('0'), Suite.SPADES)
        ])
        self.assertEqual(2, cribbage_hand.number_of_fifteen_twos())
