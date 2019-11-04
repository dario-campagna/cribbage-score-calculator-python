import sys
from cribbage.score import score
from cribbage.parse import parse_hand


def compute_score(hand_as_string):
    points = score(parse_hand(hand_as_string))
    print('The score is ' + str(points))


if __name__ == "__main__":
    compute_score(sys.argv[1])
