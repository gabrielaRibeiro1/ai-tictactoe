from games.game_simulator import GameSimulator
from games.tictactoe.players.OffensiveGreedy import OfensiveTicTacToePlayer
from games.tictactoe.simulator import TicTacToeSimulator
from games.tictactoe.players.human import HumanTicTacToePlayer

from games.tictactoe.players.minimax import MinimaxTicTacToePlayer

from games.tictactoe.players.random import RandomTicTacToePlayer


def run_simulation(desc: str, simulator: GameSimulator, iterations: int):
    print(f"----- {desc} -----")

    for i in range(0, iterations):
        simulator.change_player_positions()
        simulator.run_simulation()

    print("Results for the game:")
    simulator.print_stats()

def main():
    print("ESTG IA Games Simulator")
    #num_iterations = 100
    
    #run_simulation("name", TicTacToeSimulator(HumanTicTacToePlayer("player1"), HumanTicTacToePlayer("player2")), num_iterations)

    #tic = TicTacToeSimulator(HumanTicTacToePlayer("player1"), HumanTicTacToePlayer("player2"))

    tic = TicTacToeSimulator(HumanTicTacToePlayer("player1"), OfensiveTicTacToePlayer("player2"))

    tic.run_simulation()


if __name__ == "__main__":
    main()
