import asyncio

from poke_env import RandomPlayer
from poke_env.player import Player
from max_damage_agent import MaxDamagePlayer
from poke_env.player.baselines import MaxBasePowerPlayer
from minimax_agent import MinimaxPlayer



player1 = MaxDamagePlayer()
player2 = RandomPlayer(save_replays=False)
player3 = MaxBasePowerPlayer(save_replays=False)
player4 = MinimaxPlayer()

async def main():
    # await player1.send_challenges("testingforme", n_challenges=1)
    await player1.battle_against(player2, n_battles=10)
    
    print(
        f"Player {player1.username} won {player1.n_won_battles} out of {player1.n_finished_battles} played"
    )

asyncio.run(main())
