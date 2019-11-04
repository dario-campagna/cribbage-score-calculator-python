import sys
from cribbage.score import score
from cribbage.parse import parse_hand


def main(hand_as_string):
    points = score(parse_hand(hand_as_string))
    print('The score is ' + str(points))


if __name__ == "__main__":
    main(sys.argv[1])
