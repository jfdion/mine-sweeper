
from minesweeper.grid import Grid


class Board:

    def __init__(self, width, height, number_of_mines=10):
        self.__width = width
        self.__height = height
        self.__number_of_mines = number_of_mines
        self.__grid = Grid(self.__width, self.__height, self.__number_of_mines)

    def width(self):
        return self.__width

    def height(self):
        return self.__height

    def print(self):
        print(self.__grid.to_string())

    def win(self):
        return self.__grid.check_win()

    def loose(self):
        return self.__grid.check_mine_revealed()

    def reveal(self, x, y):
        self.__grid.reveal(x, y)

