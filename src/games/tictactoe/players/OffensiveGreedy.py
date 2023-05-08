import random

from games.tictactoe.action import TicTacToeAction
from games.tictactoe.player import TicTacToePlayer
from games.state import State
from games.tictactoe.state import TicTacToeState


class OfensiveTicTacToePlayer(TicTacToePlayer):
    RANDOM_POSITIONS = [
        (1, 1),
        (1, 20),
        (20, 1),
        (20, 20)
    ]

    def __init__(self, player_num):
        super().__init__(f"GreedyPlayer{player_num}")
        self.player_num = player_num

        """
               list of moves
               """
        self.__players_moves = [[], []]

    def is_first_play(self, state: TicTacToeState):
        if not isinstance(state, TicTacToeState):
            raise TypeError("state must be an instance of TicTacToeState")

        for row in range(state.get_num_rows()):
            for col in range(state.get_num_cols()):
                if state.get_grid() != TicTacToeState.EMPTY_CELL:
                    return False
        return True

    def save_last_play(self,  action: TicTacToeAction):
        row = action.get_row()
        col = action.get_col()

        self.__players_moves[self.player_num].append([row, col])
        return self.__players_moves[self.player_num]

    def get_possible_actions(self, state: TicTacToeState, action : TicTacToeAction):
        # Check if last action is not None
            # receive list of last move
            players_moves = self.save_last_play(action)
            last_move = players_moves[-1]

            # see possible moves for this point
            real_coord = state.convert_to_position(last_move[0], last_move[1])

            # choose a random point
            action_coord = random.choice(real_coord)

            return action_coord

    def get_action(self, state: TicTacToeState, action :TicTacToeAction):
        # if it's the first move
        if self.is_first_play(state):
            corner = random.choice(self.RANDOM_POSITIONS)
            return TicTacToeAction(corner[0], corner[1])
        else:
            chosen_position = random.choice(self.get_possible_actions(state, action))
            state.display()
            return TicTacToeAction(chosen_position[0], chosen_position[1])
    def event_action(self, pos: int, action, new_state: State):
        # ignore
        pass

    def event_end_game(self, final_state: State):
        # ignore
        pass
