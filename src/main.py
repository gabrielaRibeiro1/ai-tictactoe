from games.game_simulator import GameSimulator
from games.tictactoe.simulator import TicTacToeSimulator
from games.tictactoe.players.human import HumanTicTacToePlayer
from games.tictactoe.players.OffensiveGreedy import GreedyTicTacToePlayer
from games.tictactoe.players.minimax import MinimaxTicTacToePlayer
from src.games.tictactoe.players.DefensiveGreedy import DefensiveGreedyPlayer
from src.games.tictactoe.players.random import RandomTicTacToePlayer


def run_simulation(desc: str, simulator: GameSimulator, iterations: int):
    print(f"----- {desc} -----")

    for i in range(0, iterations):
        simulator.change_player_positions()
        simulator.run_simulation()

    print("Results for the game:")
    simulator.print_stats()



def main():
    print("ESTG IA Games Simulator")

    num_iterations = 100
    tictactoe_simulations = [
        {
            "name": "TICTACTOE : DEFENSIVE GREEDY - MINIMAX",
            "player1": DefensiveGreedyPlayer("Defensive bot"),
            "player2": MinimaxTicTacToePlayer("Minimax")
        },
        {
            "name": "TICTACTOE : OFENSIVE GREEDY - MINIMAX",
            "player1": GreedyTicTacToePlayer("Ofensive bot"),
            "player2": MinimaxTicTacToePlayer("Minimax")
        },
        {
            "name": "TICTACTOE : OFENSIVE GREEDY - HUMAN",
            "player1": HumanTicTacToePlayer("Human"),
            "player2": GreedyTicTacToePlayer("Ofensive bot")
        },
        {
            "name": "TICTACTOE : DEFENSIVE GREEDY - HUMAN",
            "player1": HumanTicTacToePlayer("Human"),
            "player2": DefensiveGreedyPlayer("Defensive bot")
        },
        {
            "name": "TICTACTOE : DEFENSIVE GREEDY - RANDOM",
            "player1": RandomTicTacToePlayer("Random"),
            "player2": DefensiveGreedyPlayer("Defensive bot")
        },
        {
            "name": "TICTACTOE : OFENSIVE GREEDY - RANDOM",
            "player1": RandomTicTacToePlayer("Random"),
            "player2": GreedyTicTacToePlayer("Ofensive bot")
        },
        {
            "name": "HUMAN - RANDOM",
            "player1": RandomTicTacToePlayer("Random"),
             "player1": HumanTicTacToePlayer("Human"),
        }
    ]

    for sim in tictactoe_simulations:
        run_simulation(sim["name"], TicTacToeSimulator(sim["player1"], sim["player2"]), num_iterations)


if __name__ == "__main__":
    main()
