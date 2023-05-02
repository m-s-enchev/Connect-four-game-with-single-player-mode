import unittest
from game_logic import *
from unittest.mock import patch
from io import StringIO
import sys


class TestPlayerMove(unittest.TestCase):
    def setUp(self) -> None:
        self.matrix = [[0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0]]
        self.player = 1





    # def test_input_not_int(self):
    #     with patch('builtins.input', side_effect=['foo']):
    #         with self.assertRaises(ValueError) as val_er:
    #             result = player_move(self.matrix, self.player)
    #         self.assertEqual(str(val_er.exception), 'Please use numeric digits.')


class TestWinConditions(unittest.TestCase):
    def setUp(self) -> None:
        self.player = 1
        self.matrix = [[1, 0, 0, 1, 0],
                       [1, 1, 1, 0, 0],
                       [1, 1, 1, 1, 0],
                       [1, 0, 0, 1, 0],
                       [0, 0, 0, 0, 0]]

    def test_check_win_horizontal(self):
        result = check_win_horizontal(self. matrix, self.player)
        self.assertEqual(result, True)

    def test_check_win_vertical(self):
        result = check_win_vertical(self. matrix, self.player)
        self.assertEqual(result, True)

    def test_check_win_right_diagonal(self):
        result = check_win_right_diagonal(self. matrix, self.player)
        self.assertEqual(result, True)

    def test_check_win_left_diagonal(self):
        result = check_win_right_diagonal(self.matrix, self.player)
        self.assertEqual(result, True)

    def test_check_for_a_tie(self):
        self.matrix = [[1, 1, 1, 1, 1],
                       [1, 1, 1, 1, 1],
                       [1, 1, 1, 1, 1],
                       [1, 1, 1, 1, 1],
                       [1, 1, 1, 1, 1]]
        result = check_for_a_tie(self.matrix)
        self.assertEqual(result, True)


class TestChooseNumberOfRows(unittest.TestCase):
    @patch('builtins.input', side_effect=['4', 'foo', '5'])
    def test_choose_number_of_rows(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.assertEqual(choose_number_of_rows(), 5)
            self.assertEqual(fake_output.getvalue().strip(), 'Invalid choice!\nPlease use numeric digits.')


if __name__ == '__main__':
    unittest.main()
