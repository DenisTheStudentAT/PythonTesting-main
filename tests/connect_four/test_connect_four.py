import pytest

from testing_course.connect_four.connect_four_game import ConnectFourGame
from testing_course.connect_four.player import Player


@pytest.fixture
def game() -> ConnectFourGame:
    return ConnectFourGame(Player.RED)


def test_correct_game_init(game: ConnectFourGame) -> None:
    assert game.player_on_turn is Player.RED
    assert not game.is_game_over
    assert game.winner is Player.NONE

    assert all(
        game.get_player_at(row, col) is Player.NONE
        for row in range(6)
        for col in range(7)
    )


def test_players_change_turns(game: ConnectFourGame) -> None:
    game.drop(1)
    assert game.get_player_at(5, 1) is Player.RED
    assert game.player_on_turn is Player.YELLOW

    game.drop(2)
    assert game.get_player_at(5, 2) is Player.YELLOW
    assert game.player_on_turn is Player.RED


def test_reset_clears_board_and_sets_starting_player(game: ConnectFourGame) -> None:
    game.drop(1)
    game.drop(2)

    game.reset(Player.YELLOW)

    assert game.player_on_turn is Player.YELLOW
    assert game.winner is Player.NONE
    assert not game.is_game_over
    assert all(
        game.get_player_at(row, col) is Player.NONE
        for row in range(6)
        for col in range(7)
    )


def test_played_fields_are_asigned_to_correct_players(game: ConnectFourGame) -> None:
    game.drop(1)
    assert game.get_player_at(5, 1) is Player.RED

    game.drop(1)
    assert game.get_player_at(5, 1) is Player.RED
    assert game.get_player_at(4, 1) is Player.YELLOW
    assert game.player_on_turn is Player.RED


def test_raise_value_error_and_same_player_plays_again(game: ConnectFourGame) -> None:

    with pytest.raises(ValueError, match="Incorrect value!"):
        game.drop(-1)

    assert game.player_on_turn is Player.RED

    with pytest.raises(ValueError, match="Incorrect value!"):
        game.drop(7)

    assert game.player_on_turn is Player.RED


def test_players_wins_vertical(game: ConnectFourGame) -> None:
    game.drop(1)  # Red 1 move
    game.drop(2)  # Yellow 1 move

    game.drop(1)  # Red 2 move
    game.drop(2)  # Yellow 2 move

    game.drop(1)  # Red 3 move
    game.drop(2)  # Yellow 3 move

    game.drop(1)  # Red 4 winning move

    assert game.winner is Player.RED
    assert game.is_game_over is True


def test_players_wins_horizontal(game: ConnectFourGame) -> None:
    game.drop(1)  # Red 1 move
    game.drop(1)  # Yellow 1 move

    game.drop(2)  # Red 2 move
    game.drop(2)  # Yellow 2 move

    game.drop(3)  # Red 3 move
    game.drop(3)  # Yellow 3 move

    game.drop(4)  # Red 4 winning move

    assert game.winner is Player.RED
    assert game.is_game_over is True


def test_player_wins_diagonally(game: ConnectFourGame) -> None:
    game.drop(0)  # RED (5,0)
    # first value for diagonal
    assert game.get_player_at(5, 0) is Player.RED

    game.drop(1)  # YELLOW (5,1)
    game.drop(1)  # RED (4,1)
    # second value for diagonal
    assert game.get_player_at(4, 1) is Player.RED

    game.drop(2)  # YELLOW (5,2)
    game.drop(2)  # RED (4,2)
    game.drop(3)  # YELLOW (5,3)
    game.drop(2)  # RED (3,2)
    # thid value for diagonal
    assert game.get_player_at(3, 2) is Player.RED

    game.drop(3)  # YELLOW (5,3)
    game.drop(3)  # RED (4,3)
    game.drop(5)  # YELLOW (5,5) -> if drop(4) yellow wins
    game.drop(3)  # RED (2,3)
    # fourth value for diagonal
    assert game.get_player_at(2, 3) is Player.RED

    assert game.winner is Player.RED
    assert game.is_game_over is True


def test_player_drops_over_the_size_of_gamefield(game: ConnectFourGame) -> None:
    game.drop(1)  # Red 1 move
    game.drop(1)  # Yellow 1 move

    game.drop(1)  # Red 2 move
    game.drop(1)  # Yellow 2 move

    game.drop(1)  # Red 3 move
    game.drop(1)  # Yellow 3 move

    with pytest.raises(ValueError, match="Column is full!"):
        game.drop(1)


def test_drops_after_game_is_won_not_registered(game: ConnectFourGame) -> None:
    game.drop(1)  # Red 1 move
    game.drop(2)  # Yellow 1 move

    game.drop(1)  # Red 2 move
    game.drop(2)  # Yellow 2 move

    game.drop(1)  # Red 3 move
    game.drop(2)  # Yellow 3 move

    game.drop(1)  # Red 4 winning move
    game.drop(2)  # Yellow 4 move

    assert game.is_game_over is True
    assert game.get_player_at(2, 2) is Player.NONE
