#
# Write a warships game with field 5x5
import random


class GameBoard:

    game_field = []

    def __init__(self):
        for i in range(5):
            GameBoard.game_field.append(["     "] * 5)
        self.ship = (random.randint(1, 5), random.randint(1, 5))

    def print_game_field(self):
        border = "+-----+-----+-----+-----+-----+"
        for i in range(5):
            print(border)
            field_str = "|".join(GameBoard.game_field[i])
            print(f"|{field_str}|")
        print(border)

    def get_ship(self):
        return self.ship

    def set_shot(self, a, b):
        GameBoard.game_field[a-1][b-1] = "X".center(5)

    def set_win_shot(self, a, b):
        GameBoard.game_field[a-1][b-1] = "WIN".center(5)


Game = GameBoard()
print(Game.ship)
Game.print_game_field()

x, y = -1, -1
while (x, y) != Game.ship:
    x, y = map(int, input(
        "Введите координаты ячейки для удара в формате x(номер ячейки по горизонтали) y(номер ячейки по вертикали): ").split())
    Game.set_shot(x, y)
    Game.print_game_field()
    print("You missed, try again")
else:
    Game.set_win_shot(x, y)
    Game.print_game_field()
    print("Congratulation, You win")
