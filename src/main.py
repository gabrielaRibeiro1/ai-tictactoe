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
    print("\n----ESTG IA Games Simulator----")
    print("\nAuthors - Gabriela Ribeiro , Nuno Lopes")
    print("\nRules:The players take turns placing pegs of their respective colors on the board, one peg per turn.\nThe player with the lighter color makes the first move.\nA player may not place a peg on their opponent's border rows.\nThe player that draws a line from one border to the other wins.\n")

    num_iterations = 30

    twixt_simulations = [

        {
            "name": "Twixt : OFENSIVE  - HUMAN",

            "player1": HumanTwixtPlayer("Human"),
            "player2": OffensiveTwixtPlayer("Ofensive bot")
        },
        {
            "name": "Twixt : DEFENSIVE  - HUMAN",
            "player1": HumanTwixtPlayer("Human"),
            "player2": DefensiveTwixtPlayer("Defensive bot")
        },
        {
            "name": "Twixt : DEFENSIVE  - RANDOM",
            "player1": RandomTwixtPlayer("Random"),
            "player2": DefensiveTwixtPlayer("Defensive bot")
        },
        {
            "name": "Twixt : OFENSIVE  - RANDOM",
            "player1": RandomTwixtPlayer("Random"),
            "player2": OffensiveTwixtPlayer("Ofensive bot")
        },
        {
            "name": "HUMAN - RANDOM",
            "player1": RandomTwixtPlayer("Random"),
            "player1": HumanTwixtPlayer("Human"),
        }
    ]

    for sim in twixt_simulations:
        run_simulation(sim["name"], TwixtSimulator(sim["player1"], sim["player2"]), num_iterations)


if __name__ == "__main__":
    main()
