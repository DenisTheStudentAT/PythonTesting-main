from typing import Protocol

from testing_course.connect_four.player import Player


class InvalidMoveError(Exception):
    """Raised when a disc cannot be dropped (full column or finished game)."""


class ConnectFour(Protocol):
    def get_player_at(self, row: int, col: int) -> Player: ...

    @property
    def player_on_turn(self) -> Player: ...

    @property
    def is_game_over(self) -> bool: ...

    @property
    def winner(self) -> Player: ...

    def reset(self, player_on_turn: Player) -> None: ...

    def drop(self, col: int) -> None: ...
