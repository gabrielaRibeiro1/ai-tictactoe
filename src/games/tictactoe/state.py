from pprint import pprint
from typing import Optional, List, Tuple

from colors import Colors
from games.tictactoe.action import TicTacToeAction
from games.tictactoe.result import TicTacToeResult
from games.state import State

HORSE_POSITIONS = [
    # top left
    (-2, 1),
    (-1, -2),

    # top right
    (1, 2),
    (2, 1),

    # bot right
    (2, -1),
    (1, -2),

    # bot left
    (-2, 1),
    (-1, 2)
]


class TicTacToeState(State):
    EMPTY_CELL = -1

    def __init__(self, num_cols: int = 24):
        super().__init__()

        if num_cols < 24:
            raise Exception("the number of cols and rows must be 24")

        """
        the dimensions of the board
        """
        self.__num_cols = num_cols
        self.__num_rows = num_cols

        """
        the grid
        """
        self.__grid = [[TicTacToeState.EMPTY_CELL for _i in range(self.__num_cols)] for _j in range(self.__num_rows)]

        """
        counts the number of turns in the current game
        """
        self.__turns_count = 1

        """
        the index of the current acting player
        """
        self.__acting_player = 0

        """
        determine if a winner was found already 
        """
        self.__has_winner = False

    def get_rows(self, action: TicTacToeAction):
        return action.get_row()

    def get_cols(self, action: TicTacToeAction):
        return action.get_col()

    def __check_winner(self, player):
        # TODO!: see if the players pieces go from one bord to the other one
        lines = []

        for col_n in range(self.get_num_cols()):
            if self.__grid[0][col_n] != self.EMPTY_CELL and self.__grid[23][col_n] != self.EMPTY_CELL:
                lines = self.get_lines()
                print(lines)

        sorted_lines = sorted(lines, key=lambda coord: coord[1])

        for i in range(1, len(sorted_lines)):
            curr_coord = sorted_lines[i]
            prev_coord = sorted_lines[i - 1]
            if curr_coord[0] != prev_coord[0] + 1:
                print(curr_coord, prev_coord)
                return False
            else:
                return True

        for row_n in range(self.get_num_rows()):
            if self.__grid[row_n][0] != self.EMPTY_CELL and self.__grid[row_n][23] != self.EMPTY_CELL:
                lines = self.get_lines()
                print(lines)

        sorted_lines = sorted(lines, key=lambda coord: coord[0])

        for i in range(1, len(sorted_lines)):
            curr_coord = sorted_lines[i]
            prev_coord = sorted_lines[i - 1]
            if curr_coord[0] != prev_coord[0] + 1:
                print(curr_coord, prev_coord)
                return False
            else:
                return True

    def get_grid(self):
        return self.__grid

    def get_num_players(self):
        return 2

    def _check_if_is_first_play(self):
        for row_n in range(self.get_num_rows()):
            for col_n in range(self.get_num_cols()):
                if self.__grid[row_n][col_n] == self.__acting_player:
                    return False
        return True

    # andre
    def convert_to_position(self, row, col):
        real_positions = []
        for position in HORSE_POSITIONS:
            real_row = row + position[0]
            real_col = col + position[1]

            if real_row < self.get_num_rows() and real_col < self.get_num_cols():
                real_positions.append((real_row, real_col))

        return real_positions

    def get_lines_for_position(self, row, col):
        lines = []
        for position in self.convert_to_position(row, col):
            if self.__grid[position[0]][position[1]] == self.__acting_player:
                lines.append(((row, col), (position[0], position[1])))

        return lines

    def get_lines(self):
        lines = []
        for row_n in range(self.get_num_rows()):
            for col_n in range(self.get_num_cols()):
                  if self.__grid[row_n][col_n] == self.__acting_player:
                    lines.extend(self.get_lines_for_position(row_n, col_n))

        self.merge_lines(lines)
        pprint(lines)
        return lines

    def merge_lines_equal_coordinates(self, n_tuple, n2_tuple):
        new_line = None

        if n_tuple[0] == n2_tuple[0]:
            new_line = (n_tuple[1], n2_tuple[1])
        elif n_tuple[1] == n2_tuple[1]:
            new_line = (n_tuple[0], n2_tuple[1])
        elif n_tuple[0] == n2_tuple[1]:
            new_line = (n_tuple[1], n2_tuple[0])
        elif n_tuple[1] == n2_tuple[0]:
            new_line = (n_tuple[0], n2_tuple[1])

        return new_line

    def merge_lines(self, lines: List[Tuple[Tuple[int, int], Tuple[int, int]]]):
        for line_n in range(len(lines) - 1):
            for line_n2 in range(line_n + 1, len(lines)):
                print(range(line_n + 1, len(lines)))
                n_tuple = lines[line_n]
                n2_tuple = lines[line_n2]

                new_line = self.merge_lines_equal_coordinates(n_tuple, n2_tuple)
                if new_line is not None:
                    lines.append(new_line)

    def validate_action(self, action: TicTacToeAction) -> bool:
        col = action.get_col()
        row = action.get_row()

        # se for a primeira jogada do jogador
        if self._check_if_is_first_play():
            if col == 0 or col == self.__num_cols:
                return False

            if row == 0 or row == self.__num_rows:
                return False

        # valid column
        if col < 0 or col >= self.__num_cols:
            return False

        # valid row
        if row < 0 or row >= self.__num_rows:
            return False

        # full column
        if self.__grid[row][col] != TicTacToeState.EMPTY_CELL:
            return False

        return True


    def update(self, action: TicTacToeAction):
        col = action.get_col()
        row = action.get_row()

        # drop the checker
        self.__grid[row][col] = self.__acting_player

        # determine if there is a winner
        self.__has_winner = self.__check_winner(self.__acting_player)

        # switch to next player
        self.__acting_player = 1 if self.__acting_player == 0 else 0

        self.__turns_count += 1

    def __display_cell(self, row, col):
        print({
                  0: f'{Colors.RED}R{Colors.END}',
                  1: f'{Colors.BLUE}B{Colors.END}',
                  TicTacToeState.EMPTY_CELL: ' '
              }[self.__grid[row][col]], end="")

    def __display_numbers(self):
        for col in range(0, self.__num_cols):
            if col == 0:
                print('  ', end="")
            if 0 < col < 9:
                print('   ', end="")
            if col == 8:
                print(' ', end="")
            if col > 8:
                print('  ', end="")
            print(col, end="")
        print("")

    def __display_separator(self):
        for col in range(0, self.__num_cols):
            print("----", end="")
        print("-")

    def display(self):
        self.__display_numbers()
        self.__display_separator()

        for row in range(0, self.__num_rows):
            print('|', end="")
            for col in range(0, self.__num_cols):
                self.__display_cell(row, col)
                print('|', end="")
            print("")
            self.__display_separator()

        self.__display_numbers()
        print("")

        pprint(self.get_lines())

    def __is_full(self):
        for row in range(self.__num_rows):
            for col in range(self.__num_cols):
                if self.__grid[row][col] == TicTacToeState.EMPTY_CELL:
                    return False
        return True

    def is_finished(self) -> bool:
        return self.__has_winner or self.__is_full()

    def get_acting_player(self) -> int:
        return self.__acting_player

    def clone(self):
        cloned_state = TicTacToeState(self.__num_cols)
        cloned_state.__turns_count = self.__turns_count
        cloned_state.__acting_player = self.__acting_player
        cloned_state.__has_winner = self.__has_winner
        for row in range(0, self.__num_rows):
            for col in range(0, self.__num_cols):
                cloned_state.__grid[row][col] = self.__grid[row][col]
        return cloned_state

    def get_result(self, pos) -> Optional[TicTacToeResult]:
        if self.__has_winner:
            return TicTacToeResult.LOOSE if pos == self.__acting_player else TicTacToeResult.WIN
        if self.__is_full():
            return TicTacToeResult.DRAW
        return None

    def get_num_rows(self):
        return self.__num_rows

    def get_num_cols(self):
        return self.__num_cols

    def before_results(self):
        pass

    def sim_play(self, action):
        new_state = self.clone()
        new_state.play(action)
        return new_state