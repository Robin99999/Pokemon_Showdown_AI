# import sys
# sys.path.append("../src")

import asyncio

from poke_env import RandomPlayer
# from poke_env.data import GenData

player1 = RandomPlayer(save_replays=False)
player2 = RandomPlayer()

async def main():

    await player1.battle_against(player2, n_battles=3)

asyncio.run(main())

print(
    f"Player {player1.username} won {player1.n_won_battles} out of {player1.n_finished_battles} played"
)