import unittest
from unittest.mock import patch
from cribbage import __main__


class TestMain(unittest.TestCase):
    @patch('builtins.print')
    def test_compute_score(self, mock_print):
        __main__.compute_score('5♥5♦5♣J♠5♠')
        mock_print.assert_called_with('The score is 29')
