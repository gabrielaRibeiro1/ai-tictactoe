from games.tictactoe.action import TicTacToeAction
from games.tictactoe.players.OffensiveGreedy import GreedyTicTacToePlayer


class DefensiveGreedyPlayer(GreedyTicTacToePlayer):
    @classmethod
    def get_score_for_position(cls, state, position: TicTacToeAction):
        number_of_chips = 0
        grid = state.get_grid()

        # verificar linha
        for idx_row in range(state.get_num_rows()):
            if grid[idx_row][position.get_col()] != state.get_acting_player():
                number_of_chips += 1

        # verificar coluna
        for idx_col in range(state.get_num_cols()):
            if grid[position.get_row()][idx_col] != state.get_acting_player():
                number_of_chips += 1

        # verificar diagonais

        #  o ponto a verificar é uma diagonal
        if (position.get_row(), position.get_col(),) in cls.CORNERS:
            # verificar diagonal crescente (0,0) (1,1) (2,2)
            for idx_row, idx_col in zip(range(state.get_num_rows()), range(state.get_num_cols())):
                if grid[idx_row][idx_col] != state.get_acting_player():
                    number_of_chips += 1

            # verificar diagonal decrescente (0, 2) (1, 1) (2, 0)
            for idx_row, idx_col in zip(range(state.get_num_rows()), range(state.get_num_cols() - 1, -1, -1)):
                if grid[idx_row][idx_col] != state.get_acting_player():
                    number_of_chips += 1
        return number_of_chips