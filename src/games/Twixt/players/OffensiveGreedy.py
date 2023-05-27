import random

from games.Twixt.action import TwixtAction
from games.Twixt.player import TwixtPlayer
from games.state import State
from games.Twixt.state import TwixtState


class OffensiveTwixtPlayer(TwixtPlayer):
    RANDOM_POSITIONS = [
        (1, 1),
        (1, 20),
        (20, 1),
        (20, 20)
    ]

    def __init__(self, player_num):
        super().__init__(f"GreedyPlayer{player_num}")
        self.player_num = player_num


    def get_possible_actions(self, state: TwixtState):
        players_moves = state.save_last_play()
        last_move = players_moves[-1]
        print(last_move)

        # ver possiveis movimentos para esse ponto
        real_coord = state.convert_to_position(last_move[0], last_move[1])
        print(real_coord)

        return real_coord

    def get_action(self, state: TwixtState):

        # if it's the first move
        for row in range(state.get_num_rows()):
            for col in range(state.get_num_cols()):
                if state.get_grid()[row][col] != TwixtState.EMPTY_CELL:
                 corner = random.choice(self.RANDOM_POSITIONS)
                 return TwixtAction(corner[0], corner[1])
        else:
            chosen_position = random.choice(self.get_possible_actions(state))
            return TwixtAction(chosen_position[0], chosen_position[1])

    def event_action(self, pos: int, action, new_state: State):
        # ignore
        pass

    def event_end_game(self, final_state: State):
        # ignore
        pass
