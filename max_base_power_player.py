import asyncio

from poke_env import RandomPlayer
from poke_env.player.baselines import MaxBasePowerPlayer

player1 = MaxBasePowerPlayer(save_replays=False)
player2 = RandomPlayer()

async def main():

    await player1.battle_against(player2, n_battles=100)

asyncio.run(main())

print(
    f"Player {player1.username} won {player1.n_won_battles} out of {player1.n_finished_battles} played"
)