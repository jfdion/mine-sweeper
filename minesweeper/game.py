from minesweeper.board import Board
import sys


class Game:
    __game_state = "new"

    def __init__(self):
        self.__running = False
        self.__board = None

    def start(self):
        if self.__game_state != "new":
            self.__input_start_new_game()
        col_count = self.__input_col_count()
        row_count = self.__input_row_count()
        mines_count = self.__input_mine_count(col_count, row_count)

        self.__running = True
        self.__game_state = "started"
        self.__board = Board(col_count, row_count, mines_count)
        self.__board.print()
        self.finished()

    def update(self):
        if not self.running():
            return
        reveal_x = self.__input_reveal_x()
        reveal_y = self.__input_reveal_y()

        self.__board.reveal(reveal_x, reveal_y)
        self.__board.print()
        self.finished()

    def finished(self):
        if self.__board.win() or self.__board.loose():
            self.end()

    def end(self):
        self.__running = False
        if self.__board.win() and not self.__board.loose():
            print("YOU WON!!")
        else:
            print("YOU LOST!!")

    def running(self):
        return self.__running

    def __input_reveal_y(self):
        while True:
            reveal_y = input("Reveal (y) : ")
            if int(reveal_y) and 1 <= int(reveal_y) <= self.__board.height():
                reveal_y = int(reveal_y) - 1
                break
        return reveal_y

    def __input_reveal_x(self):
        while True:
            reveal_x = input("Reveal (x) : ")
            if int(reveal_x) and 1 <= int(reveal_x) <= self.__board.width():
                reveal_x = int(reveal_x) - 1
                break
        return reveal_x

    def __input_mine_count(self, col_count, row_count):
        while True:
            mines_count = input("Number of mines: ")
            if int(mines_count) and 0 < int(mines_count) <= col_count * row_count:
                mines_count = int(mines_count)
                break
        return mines_count

    def __input_row_count(self):
        while True:
            row_count = input("Number of rows: ")
            if int(row_count) and int(row_count) > 1:
                row_count = int(row_count)
                break
        return row_count

    def __input_col_count(self):
        while True:
            col_count = input("Number of columns: ")
            if int(col_count) and int(col_count) > 1:
                col_count = int(col_count)
                break
        return col_count

    def __input_start_new_game(self):
        while True:
            new_game = input("Start a new game? Y/N (Y): ")
            if new_game == "" or new_game.upper() == "Y":
                break
            elif new_game.upper() == "N":
                sys.exit(0)
