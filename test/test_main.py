import unittest
from unittest.mock import patch
from production.cribbage_score_calculator import main


class TestMain(unittest.TestCase):
    @patch('builtins.print')
    def test_compute_score(self, mock_print):
        main('5♥5♦5♣J♠5♠')
        mock_print.assert_called_with('The score is 29')
