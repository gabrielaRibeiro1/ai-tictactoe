from games.Twixt.players.DefensiveGreedy import DefensiveTwixtPlayer
from games.game_simulator import GameSimulator
from games.Twixt.players.OffensiveGreedy import OffensiveTwixtPlayer
from games.Twixt.simulator import TwixtSimulator
from games.Twixt.players.human import HumanTwixtPlayer

from games.Twixt.players.minimax import MinimaxTwixtPlayer

from games.Twixt.players.random import RandomTwixtPlayer


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

    twixt_simulations = [
        
        {

            "name": "Twixt - Human VS Random",
            "player1": HumanTwixtPlayer("Human"),
            "player2": DefensiveTwixtPlayer("Random")
        }
    ]

    for sim in twixt_simulations:
        run_simulation(sim["name"], TwixtSimulator(sim["player1"], sim["player2"]), num_iterations)


if __name__ == "__main__":
    main()
