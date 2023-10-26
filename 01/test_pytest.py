import io
import contextlib
from main import TicTacToe, input_dimension


def test_validate_input():
    game = TicTacToe()
    assert game.validate_input(0, 0)
    assert game.validate_input(0, 1)
    assert game.validate_input(0, 2)
    assert game.validate_input(1, 2)


def test_validate_input_out_of_bounds():
    game = TicTacToe()
    assert not game.validate_input(-1, 0)
    assert not game.validate_input(0, -1)
    assert not game.validate_input(3, 0)
    assert not game.validate_input(0, 6)


def test_validate_input_already_taken():
    game = TicTacToe()
    game.matrix = [['x', 'o', '*'], ['*', 'x', '*'], ['*', '*', 'o']]
    assert not game.validate_input(0, 0)
    assert not game.validate_input(1, 1)
    assert not game.validate_input(2, 2)


def test_check_side_x(monkeypatch):
    game = TicTacToe()
    monkeypatch.setattr('builtins.input', lambda: 'x')
    assert game.check_side()
    assert game.side == 'x'


def test_check_side_o(monkeypatch):
    game = TicTacToe()
    monkeypatch.setattr('builtins.input', lambda: 'o')
    assert game.check_side()
    assert game.side == '0'


def test_check_side_invalid(monkeypatch):
    game = TicTacToe()
    monkeypatch.setattr('builtins.input', lambda: 'invalid')
    assert not game.check_side()


def test_enter_coordinates(monkeypatch):
    game = TicTacToe()
    user_input = '1 1\n'
    monkeypatch.setattr('builtins.input', lambda: user_input)
    result = game.enter_coordinates()
    assert result == (0, 0)


def test_enter_coordinates_invalid(monkeypatch):
    def mock_input():
        return next(user_inputs)
    game = TicTacToe()
    user_inputs = iter(['a b', '1 2'])
    monkeypatch.setattr('builtins.input', mock_input)
    with io.StringIO() as mock_stdout:
        with contextlib.redirect_stdout(mock_stdout):
            result = game.enter_coordinates()
    assert result == (0, 1)


def test_change_side():
    game = TicTacToe()
    game.side = 'x'
    game.change_side()
    assert game.side == '0'
    game.change_side()
    assert game.side == 'x'


def test_choose_side_0(monkeypatch):
    game = TicTacToe()
    monkeypatch.setattr('builtins.input', lambda: 'o')
    game.choose_side()
    assert game.side == '0'


def test_choose_side_invalid(monkeypatch):
    def mock_input():
        return next(user_inputs)
    game = TicTacToe()
    user_inputs = iter(['g', 'EE', 'X'])
    monkeypatch.setattr('builtins.input', mock_input)
    with io.StringIO() as mock_stdout:
        with contextlib.redirect_stdout(mock_stdout):
            game.choose_side()
    assert game.side == 'x'


def test_check_winner_row():
    game = TicTacToe()
    game.matrix = [['x', 'x', 'x'], ['*', '0', '0'], ['*', '*', '*']]
    result = game.check_winner(0, 0)
    assert result


def test_check_winner_column():
    game = TicTacToe()
    game.matrix = [['x', '0', '*'], ['x', '*', '*'], ['x', '0', '0']]
    result = game.check_winner(0, 0)
    assert result


def test_check_winner_main_diagonal():
    game = TicTacToe()
    game.matrix = [['x', '0', '*'], ['*', 'x', '*'], ['*', '0', 'x']]
    result = game.check_winner(1, 1)
    assert result


def test_check_winner_side_diagonal():
    game = TicTacToe()
    game.matrix = [['*', '0', 'x'], ['*', 'x', '*'], ['x', '0', '*']]
    result = game.check_winner(1, 1)
    assert result


def test_check_winner_no_winner():
    game = TicTacToe()
    game.matrix = [['x', '0', 'x'], ['0', '0', 'x'], ['0', 'x', '0']]
    result = game.check_winner(2, 2)
    assert not result


def test_play_game_draw(monkeypatch):
    def mock_input():
        return next(user_inputs)
    game = TicTacToe()
    user_inputs = iter(['x', '1 1', '1 2', '1 3', '2 1', '2 2', '3 3', '2 3', '3 1', '3 2'])
    monkeypatch.setattr('builtins.input', mock_input)
    with io.StringIO() as mock_stdout:
        with contextlib.redirect_stdout(mock_stdout):
            result = game.play_game()
    assert not result


def test_play_game_x_wins(monkeypatch):
    def mock_input():
        return next(user_inputs)
    game = TicTacToe()
    user_inputs = iter(['x', '1 1', '2 2', '2 1', '3 3', '2 3', '1 2', '3 1'])
    monkeypatch.setattr('builtins.input', mock_input)
    with io.StringIO() as mock_stdout:
        with contextlib.redirect_stdout(mock_stdout):
            result = game.play_game()
    assert result
    assert game.side == 'x'


def test_play_game_o_wins(monkeypatch):
    def mock_input():
        return next(user_inputs)
    game = TicTacToe()
    user_inputs = iter(['O', '1 1', '2 2', '2 1', '3 3', '2 3', '1 2', '3 1'])
    monkeypatch.setattr('builtins.input', mock_input)
    with io.StringIO() as mock_stdout:
        with contextlib.redirect_stdout(mock_stdout):
            result = game.play_game()
    assert result
    assert game.side == '0'


def test_input_dimension(monkeypatch):
    def mock_input():
        return next(user_inputs)
    user_inputs = iter(['2', '5.0', '11', 'abc', '7'])
    monkeypatch.setattr('builtins.input', mock_input)
    with io.StringIO() as mock_stdout:
        with contextlib.redirect_stdout(mock_stdout):
            result = input_dimension()
    assert result == 7
