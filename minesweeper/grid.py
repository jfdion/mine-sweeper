from random import randint

from minesweeper.cell import Cell


class Grid:

    def __init__(self, width, height, number_of_mines):
        self.__width = width
        self.__height = height
        self.__mines_locations = self._build_mines_locations(number_of_mines)
        self.__grid = [[Cell(x, y, self, is_mine=(x, y) in self.__mines_locations)
                        for x in range(0, self.__width)]
                       for y in range(0, self.__height)]
        [[cell.update_neighbor_count() for cell in row] for row in self.__grid]

    def init_grid_reveal_cache(self):
        return [[False] * self.__width] * self.__height

    def _build_mines_locations(self, number_of_mines):
        mines_locations = []
        i = 0
        while i < number_of_mines:
            x = randint(0, self.__width - 1)
            y = randint(0, self.__height - 1)
            if (x, y) not in mines_locations:
                mines_locations.append((x, y))
                i += 1
        return mines_locations

    def check_win(self):
        return sum([sum([0 if cell.revealed() else 1 for cell in row]) for row in self.__grid]) == len(
            self.__mines_locations)

    def check_mine_revealed(self):
        return sum([sum([1 if cell.revealed() and cell.is_mine() else 0 for cell in row]) for row in self.__grid]) > 0

    def exists(self, x, y):
        return 0 <= x < self.__width and 0 <= y < self.__height

    def is_mine(self, x, y):
        if self.exists(x, y):
            return self.__grid[y][x].is_mine()

    def reveal(self, x, y):
        if self.exists(x, y) and not self.revealed(x, y):
            self.__grid[y][x].reveal()

    def revealed(self, x, y):
        if self.exists(x, y):
            return self.__grid[y][x].revealed()
        return True

    def has_neighbor(self, x, y):
        if self.exists(x, y):
            return self.__grid[y][x].neighbor_count() > 0

    def to_string(self):

        out = "| " + (len(str(self.__height)) * " ") + " |"
        for i in range(0, self.__width):
            out += " " + (self.__calculate_padding(str(i + 1), len(str(self.__width)), 1) * " ")
            out += str(i + 1)
            out += (self.__calculate_padding(str(i + 1), len(str(self.__width)), -1) * " ") + " |"
        out += "\n"

        j = 1
        for row in self.__grid:
            out += "| " + str(j) + ((len(str(self.__height)) - len(str(j))) * " ") + " |"
            for (x, cell) in enumerate(row):
                out += " "
                out += (self.__calculate_padding(cell.to_string(), len(str(self.__width)), 1) * " ")
                out += cell.to_string()
                out += (self.__calculate_padding(cell.to_string(), len(str(self.__width)), -1) * " ") + " |"
            out += "\n"
            j += 1
        return out

    def __calculate_padding(self, text, total_length, modifier):
        size = abs(total_length - len(text))
        if size == 0:
            return size

        if modifier > 0:
            modifier = 1
        else:
            modifier = -1

        if size % 2 == 0:
            return int(size / 2)
        else:
            return int((size + modifier) / 2)
