from testing_course.connect_four.connect_four import ConnectFour
from testing_course.connect_four.connect_four_game import ConnectFourGame
from testing_course.connect_four.player import Player

HELP = """
Available commands:
-------------------
1 .. 7 --> drop disc in column
r      --> restart game
q      --> quit game
h      --> show help"""


def main() -> None:
    game: ConnectFour = ConnectFourGame(Player.RED)
    print(game)

    while not game.is_game_over:
        try:
            command = input("command [1 .. 7, (r)estart, (q)uit, (h)elp] > ")
        except EOFError:
            return

        match command:
            case "1" | "2" | "3" | "4" | "5" | "6" | "7":
                game.drop(int(command) - 1)
            case "r":
                game.reset(Player.RED)
            case "q":
                print("Ok, bye.")
                return
            case "h":
                print(HELP)
            case _:
                print("Unknown command")
        print(game)

    print(f"GAME OVER - Winner: {game.winner.name}")


if __name__ == "__main__":
    main()
