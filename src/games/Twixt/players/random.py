from random import randint

from games.Twixt.action import TwixtAction
from games.Twixt.player import TwixtPlayer
from games.Twixt.state import TwixtState
from games.state import State


class RandomTwixtPlayer(TwixtPlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: TwixtState):
        return TwixtAction(randint(0, state.get_num_cols()), randint(0, state.get_num_rows()))

    def event_action(self, pos: int, action, new_state: State):
        # ignore
        pass

    def event_end_game(self, final_state: State):
        # ignore
        pass
