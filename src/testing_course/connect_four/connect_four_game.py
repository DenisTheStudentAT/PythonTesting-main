from testing_course.connect_four.player import Player


class ConnectFourGame:
    def __init__(self, player_on_turn: Player) -> None:

        self._board: list[list[Player]] = []
        self._player_on_turn = Player.NONE
        self._winner = Player.NONE
        self.reset(player_on_turn)

    def get_player_at(self, row: int, col: int) -> Player:
        if not (0 <= row < 6 and 0 <= col < 7):
            raise ValueError("Out of boundary value")
        return self._board[row][col]

    @property
    def player_on_turn(self) -> Player:
        return self._player_on_turn

    @property
    def is_game_over(self) -> bool:
        return self._winner is not Player.NONE

    @property
    def winner(self) -> Player:
        return self._winner

    def reset(self, player_on_turn: Player) -> None:
        self._player_on_turn = player_on_turn
        self._winner = Player.NONE

        self._board = []
        for _i in range(6):
            row = [Player.NONE] * 7
            self._board.append(row)

    def drop(self, col: int) -> None:
        if col > 6 or col < 0:
            raise ValueError("Incorrect value!")
        if self._winner != Player.NONE:
            print("There is a winner already! Reset the game or quit.")
        else:
            target_row = -1
            for row in range(5, -1, -1):  # идем от 5-й строки до 0-й
                if self._board[row][col] == Player.NONE:
                    target_row = row
                    break
            if target_row == -1:
                raise ValueError("Column is full!")

            self._board[target_row][col] = self._player_on_turn

            if self.check_winner(target_row, col, self._player_on_turn):
                self._winner = self._player_on_turn

            if self._player_on_turn == Player.RED:
                self._player_on_turn = Player.YELLOW
            else:
                self._player_on_turn = Player.RED

    def check_winner(self, row: int, col: int, player: Player) -> bool:
        consecutive_vertical = 0
        for r in range(6):
            if self._board[r][col] == player:
                consecutive_vertical += 1
                if consecutive_vertical >= 4:
                    return True
            else:
                consecutive_vertical = 0

        consecutive_horizontal = 0
        for c in range(7):
            if self._board[row][c] == player:
                consecutive_horizontal += 1
                if consecutive_horizontal >= 4:
                    return True
            else:
                consecutive_horizontal = 0

        consecutive_diag1 = 0
        for i in range(-3, 4):
            r = row + i
            c = col + i
            if 0 <= r < 6 and 0 <= c < 7:
                if self._board[r][c] == player:
                    consecutive_diag1 += 1
                    if consecutive_diag1 >= 4:
                        return True
                else:
                    consecutive_diag1 = 0

        consecutive_diag2 = 0
        for i in range(-3, 4):
            r = row + i
            c = col - i
            if 0 <= r < 6 and 0 <= c < 7:
                if self._board[r][c] == player:
                    consecutive_diag2 += 1
                    if consecutive_diag2 >= 4:
                        return True
                else:
                    consecutive_diag2 = 0

        return False
