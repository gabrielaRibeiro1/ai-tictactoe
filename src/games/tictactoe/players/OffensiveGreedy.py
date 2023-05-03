import random

from games.tictactoe.action import TicTacToeAction
from games.tictactoe.player import TicTacToePlayer
from games.state import State
from games.tictactoe.state import TicTacToeState


class GreedyTicTacToePlayer(TicTacToePlayer):
    RANDOM_POSITIONS = [
        (1, 1),
        (1, 20),
        (20, 1),
        (20, 20)
    ]

    def __init__(self, player_num):
        super().__init__(f"GreedyPlayer{player_num}")
        self.player_num = player_num

    @staticmethod
    def is_first_play(state: TicTacToeState):
        for row in range(state.get_num_rows()):
            for col in range(state.get_num_cols()):
                if state.get_grid()[row][col] != TicTacToeState.EMPTY_CELL:
                    return False
        return True

    def get_possible_actions(self, state: TicTacToeState):
        #receber lista de ultimo movimento
        players_moves = state.save_last_play()
        last_move = players_moves[-1]

        #ver possiveis movimentos para esse ponto
        real_coord = state.convert_to_position(state, last_move[0], last_move[1])

        #escolher um ponto random
        action_coord = random.choice(real_coord)

        return action_coord



    @classmethod
    def get_action(cls, state: TicTacToeState):
        # se for a primeira jogada
        if cls.is_first_play(state):
            corner = random.choice(cls.RANDOM_POSITIONS)
            return TicTacToeAction(corner[0], corner[1])
        else:
            chosen_position = cls.get_best_position(state)
            state.display()
            return chosen_position

    def event_action(self, pos: int, action, new_state: State):
        # ignore
        pass

    def event_end_game(self, final_state: State):
        # ignore
        pass
