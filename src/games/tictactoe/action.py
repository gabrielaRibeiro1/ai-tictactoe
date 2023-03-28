class TicTacToeAction:
    """
    a tictactoe action is simple - it only takes the value of the column and the row to play
    """
    __col: int
    __row: int

    def __init__(self, col: int, row: int):
        self.__col = col
        self.__row = row

    def get_col(self):
        return self.__col

    def get_row(self):
        return self.__row

    def __repr__(self):
        return f'({self.__row}, {self.__col})'