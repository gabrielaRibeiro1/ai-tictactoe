from games.Twixt.action import TwixtAction
from games.Twixt.player import TwixtPlayer
from games.Twixt.state import TwixtState


class HumanTwixtPlayer(TwixtPlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: TwixtState):
        state.display()

        while True:

            # noinspection PyBroadException
            try:

                row = int(input(f"Player {state.get_acting_player()}, choose a row: "))
                col = int(input(f"Player {state.get_acting_player()}, choose a column: "))

                return TwixtAction(col, row)
            except Exception:
                continue

    def event_action(self, pos: int, action, new_state: TwixtState):
        # ignore
        pass

    def event_end_game(self, final_state: TwixtState):
        # ignore
        pass
