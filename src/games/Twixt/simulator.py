from games.Twixt.player import TwixtPlayer
from games.Twixt.state import TwixtState
from games.game_simulator import GameSimulator


class TwixtSimulator(GameSimulator):

    def __init__(self, player1: TwixtPlayer, player2: TwixtPlayer, num_cols: int = 24):
        super(TwixtSimulator, self).__init__([player1, player2])
        """
        the number of rows and cols from the Twixt grid
        """
        self.__num_rows = num_cols
        self.__num_cols = num_cols

    def init_game(self):
        return TwixtState(self.__num_cols)

    def before_end_game(self, state: TwixtState):
        # ignored for this simulator
        pass

    def end_game(self, state: TwixtState):
        # ignored for this simulator
        pass
