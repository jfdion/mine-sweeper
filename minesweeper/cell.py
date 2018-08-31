class Cell:
    """
    | (-1, -1) | (0, -1) | (1, -1) |
    | (-1, 0)  | x       | (1, 0)  |
    | (-1, 1)  | (0, 1)  | (1, 1)  |
    """
    __positions = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

    """
   |          | (0, -1) |         |
   | (-1, 0)  | x       | (1, 0)  |
   |          | (0, 1)  |         |
   """
    __cross_positions = [(0, -1), (-1, 0), (1, 0), (0, 1)]

    def __init__(self, x, y, grid, is_mine=False):
        self.__x = x
        self.__y = y
        self.__grid = grid
        self.__is_mine = is_mine
        self.__is_revealed = False
        self.__neighbor_mines = 0

    def to_string(self):
        if not self.__is_revealed:
            return "?"
        elif self.__is_mine:
            return "!"
        elif self.__neighbor_mines > 0:
            return str(self.__neighbor_mines)
        else:
            return " "

    def revealed(self):
        return self.__is_revealed

    def is_mine(self):
        return self.__is_mine

    def neighbor_count(self):
        return self.__neighbor_mines

    def update_neighbor_count(self):
        self.__neighbor_mines = 0
        if self.__is_mine:
            return
        for (x, y) in self.__positions:
            if self.__grid.exists(self.__x + x, self.__y + y) and \
                    self.__grid.is_mine(self.__x + x, self.__y + y):
                self.__neighbor_mines += 1

    def reveal(self):
        if self.__is_revealed:
            return
        self.__is_revealed = True
        if not self.__is_mine and not self.__neighbor_mines > 0:
            for (x, y) in self.__cross_positions:
                self.__grid.reveal(self.__x + x, self.__y + y)
