from games.tictactoe.player import TicTacToePlayer
from games.tictactoe.state import TicTacToeState
from games.game_simulator import GameSimulator


class TicTacToeSimulator(GameSimulator):

    def __init__(self, player1: TicTacToePlayer, player2: TicTacToePlayer, num_cols: int = 24):
        super(TicTacToeSimulator, self).__init__([player1, player2])
        """
        the number of rows and cols from the connect4 grid
        """
        self.__num_rows = num_cols
        self.__num_cols = num_cols

    def init_game(self):
        return TicTacToeState(self.__num_cols)

    def before_end_game(self, state: TicTacToeState):
        # ignored for this simulator
        pass

    def end_game(self, state: TicTacToeState):
        # ignored for this simulator
        pass