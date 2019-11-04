from production.cribbage.cards import CribbageHand


def score(cribbage_hand: CribbageHand):
    return (
        __score_fifteen_twos__(cribbage_hand) +
        __score_runs__(cribbage_hand) +
        __score_pairs__(cribbage_hand) +
        __score_flush__(cribbage_hand)
    )


def __score_fifteen_twos__(cribbage_hand):
    return 2 * cribbage_hand.number_of_fifteen_twos()


def __score_runs__(cribbage_hand):
    if cribbage_hand.is_run_of_five():
        return 5
    elif cribbage_hand.is_run_of_four():
        return 4
    else:
        return 3 * cribbage_hand.number_of_runs_of_three()


def __score_pairs__(cribbage_hand: CribbageHand):
    return 2 * cribbage_hand.number_of_pairs()


def __score_flush__(cribbage_hand: CribbageHand):
    return 4 * cribbage_hand.is_flush() + 1 * cribbage_hand.holds_nob()
