import unittest
import io
from unittest.mock import patch
from main import TicTacToe
from main import input_dimension


class TestValidateInput(unittest.TestCase):
    # метод принимает декремент от ввода (не 1 2, а 0 1)

    def setUp(self):
        self.game = TicTacToe()

    def test_input_pair_right(self):
        self.assertTrue(TicTacToe.validate_input(self.game, 1, 2))

    @patch('builtins.input', side_effect=['1 1'])
    def test_input_pair_taken(self, mock_input):
        self.game.enter_coordinates()
        self.assertFalse(TicTacToe.validate_input(self.game, 0, 0))

    def test_input_pair_more_than_dim(self):
        self.assertFalse(TicTacToe.validate_input(self.game, 1, 3))

    def test_input_pair_zero(self):
        self.assertTrue(TicTacToe.validate_input(self.game, 0, 1))

    def test_input_pair_negative(self):
        self.assertFalse(TicTacToe.validate_input(self.game, 2, -1))


class TestEnterCoordinates(unittest.TestCase):

    def setUp(self):
        self.game = TicTacToe()

    @patch('builtins.input', side_effect=['a b', '1 2'])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_enter_coordinates_invalid_input(self, mock_stdout, mock_input):
        expected_output = "Player for x,\nEnter two coordinates from 1 to 3, for example '1 1'\n" \
                          "  1 2 3 \n1 * * * \n2 * * * \n3 * * * \nIncorrect input! Try again!\n" \
                          "Player for x,\nEnter two coordinates from 1 to 3, for example '1 1'\n" \
                          "  1 2 3 \n1 * * * \n2 * * * \n3 * * * \n"
        i, j = self.game.enter_coordinates()
        self.assertEqual(mock_stdout.getvalue(), expected_output)
        self.assertEqual((i, j), (0, 1))

    @patch('builtins.input', side_effect=['1 1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_enter_coordinates_valid_input(self, mock_stdout, mock_input):
        expected_output = "Player for x,\nEnter two coordinates from 1 to 3, for example '1 1'\n" \
                          "  1 2 3 \n1 * * * \n2 * * * \n3 * * * \n"
        i, j = self.game.enter_coordinates()
        self.assertEqual(mock_stdout.getvalue(), expected_output)
        self.assertEqual((i, j), (0, 0))


class TestCheckSide(unittest.TestCase):

    def setUp(self):
        self.game = TicTacToe()

    @patch('builtins.input', return_value='x')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_side_x(self, mock_stdout, mock_input):
        result = self.game.check_side()
        self.assertTrue(result)
        self.assertEqual(self.game.side, "x")

    @patch('builtins.input', return_value='O')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_side_o(self, mock_stdout, mock_input):
        result = self.game.check_side()
        self.assertTrue(result)
        self.assertEqual(self.game.side, "0")

    @patch('builtins.input', return_value='invalid')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_side_invalid_input(self, mock_stdout, mock_input):
        result = self.game.check_side()
        self.assertFalse(result)


class TestChooseSide(unittest.TestCase):

    def setUp(self):
        self.game = TicTacToe()

    @patch('builtins.input', return_value='o')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_side_at_first_time(self, mock_stdout, mock_input):
        self.game.choose_side()
        self.assertEqual(self.game.side, "0")

    @patch('builtins.input', side_effect=['invalid', 'x'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_side_invalid_input_at_first(self, mock_stdout, mock_input):
        self.game.choose_side()
        self.assertEqual(self.game.side, "x")


class TestCheckWinner(unittest.TestCase):

    def setUp(self):
        self.game = TicTacToe()
        self.game.dim = 3

    def test_check_winner_row(self):
        self.game.matrix = [['x', 'x', 'x'], ['*', '0', '0'], ['*', '*', '*']]
        result = self.game.check_winner(0, 0)
        self.assertTrue(result)

    def test_check_winner_column(self):
        self.game.matrix = [['x', '0', '*'], ['x', '*', '*'], ['x', '0', '0']]
        result = self.game.check_winner(0, 0)
        self.assertTrue(result)

    def test_check_winner_main_diagonal(self):
        self.game.matrix = [['x', '0', '*'], ['*', 'x', '*'], ['*', '0', 'x']]
        result = self.game.check_winner(1, 1)
        self.assertTrue(result)

    def test_check_winner_side_diagonal(self):
        self.game.matrix = [['*', '0', 'x'], ['*', 'x', '*'], ['x', '0', '*']]
        result = self.game.check_winner(1, 1)
        self.assertTrue(result)

    def test_check_winner_no_winner(self):
        self.game.matrix = [['x', '0', 'x'], ['0', '0', 'x'], ['0', 'x', '0']]
        result = self.game.check_winner(2, 2)
        self.assertFalse(result)


class TestChangeSide(unittest.TestCase):

    def setUp(self):
        self.game = TicTacToe()

    def test_change_side_x_to_o(self):
        self.game.side = "x"
        self.game.change_side()
        self.assertEqual(self.game.side, "0")

    def test_change_side_o_to_x(self):
        self.game.side = "0"
        self.game.change_side()
        self.assertEqual(self.game.side, "x")


class TestInputDimension(unittest.TestCase):

    def setUp(self):
        self.game = TicTacToe()

    @patch('builtins.input', side_effect=['2', '5.0', '11', 'abc', '7'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_dimension(self, mock_stdout, mock_input):
        result = input_dimension()
        self.assertEqual(result, 7)


class TestPlayGame(unittest.TestCase):

    def setUp(self):
        self.game = TicTacToe()
        self.game.dim = 3

    @patch('builtins.input', side_effect=['x', '1 1', '1 2', '1 3', '2 1', '2 2', '3 3', '2 3', '3 1', '3 2'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_play_game_draw(self, mock_stdout, mock_input):
        result = self.game.play_game()
        self.assertFalse(result)

    @patch('builtins.input', side_effect=['x', '1 1', '2 2', '2 1', '3 3', '2 3', '1 2', '3 1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_play_game_x_wins(self, mock_stdout, mock_input):
        result = self.game.play_game()
        self.assertEqual(self.game.side, "x")
        self.assertTrue(result)

    @patch('builtins.input', side_effect=['O', '1 1', '2 2', '2 1', '3 3', '2 3', '1 2', '3 1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_play_game_o_wins(self, mock_stdout, mock_input):
        result = self.game.play_game()
        self.assertEqual(self.game.side, "0")
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
