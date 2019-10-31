from production.cribbage.cards import CribbageHand


def score(cribbage_hand: CribbageHand):
    return __score_pairs__(cribbage_hand) + __score_flush__(cribbage_hand)


def __score_pairs__(cribbage_hand: CribbageHand):
    return 2 * cribbage_hand.number_of_pairs()


def __score_flush__(cribbage_hand: CribbageHand):
    return 4 * cribbage_hand.is_flush() + 1 * cribbage_hand.holds_nob()
