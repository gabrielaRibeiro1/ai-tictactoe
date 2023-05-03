import random

from games.tictactoe.action import TicTacToeAction
from games.tictactoe.players.OffensiveGreedy import GreedyTicTacToePlayer
from games.tictactoe.state import TicTacToeState


class DefensiveGreedyPlayer(GreedyTicTacToePlayer):

    @classmethod
    def get_action(cls, state: TicTacToeState):
        # se for a primeira jogada
        if cls.is_first_play(state):
            corner = random.choice(cls.RANDOM_POSITIONS)
            return TicTacToeAction(corner[0], corner[1])
        else:
            chosen_position = cls.get_possible_actions(state)
            state.display()



