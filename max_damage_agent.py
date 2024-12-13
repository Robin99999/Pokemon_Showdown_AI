import asyncio
import util

# from poke_env.data import GenData, to_id_str
from poke_env.environment.abstract_battle import AbstractBattle
from poke_env.player.player import Player
from poke_env.environment.move_category import MoveCategory
from poke_env.environment.pokemon import Pokemon
from poke_env.player.battle_order import BattleOrder
from poke_env.ps_client.ps_client import PSClient
from poke_env.player.battle_order import (
    BattleOrder,
    DefaultBattleOrder,
)

class MaxDamagePlayer(Player):
    def choose_move(self, battle: AbstractBattle) -> BattleOrder:
        # return self.choose_random_move(battle)
        # print("possible moves ", battle.available_moves)
        # print('apokemon:', battle.active_pokemon, type(battle.active_pokemon))
        
        if battle.available_switches or battle.available_moves:

        
            current_mon = battle.active_pokemon
            opp_mon = battle.opponent_active_pokemon
            best_damage = 0
            if battle.available_moves:
                #keeps associated damage with move
                moves_with_damage = [
                    (move, util.calc_damage(current_mon, opp_mon, move)) 
                    for move in battle.available_moves
                ]

            # Find the best move based on the maximum damage
                best_move, best_damage = max(moves_with_damage, key=lambda x: x[1])
            # print(best_move,"dam", best_damage)
            # check if there is a better pokemon for this matchup
            
            if battle.available_switches:
                score = self.type_matchup(current_mon,opp_mon)
                b_switch = self.best_switch(battle)
                # print(score)
                # print(b_switch[1])
                if score < b_switch[1] and score <= 0 and not best_damage > 500:
                    return self.create_order(b_switch[0])



            # check if no moves available and see if switch or struggle
            if not battle.available_moves or best_damage <= 50:
                return self.choose_random_move(battle)
            

            return self.create_order(best_move)
        else:
            # print(battle.available_moves, battle.available_switches)
            # print('hi3232')
            return self.choose_random_move(battle)



    def best_switch(self, battle):
        if not battle.available_switches:
            return None
        

        best_switch = [
                (switch, self.type_matchup(switch, battle.opponent_active_pokemon))
                for switch in battle.available_switches
            ]

        best_switch, best_score = min(best_switch, key=lambda x: x[1])
        return (best_switch,best_score)
        
    #lower the num the better
    def type_matchup(self, my_pokemon:Pokemon, opponent_pokemon:Pokemon):
        # how much opponent pokemon hits into our pokemon
        score = [opponent_pokemon.damage_multiplier(t) for t in my_pokemon.types if t is not None]

        multiplier_dict = {
            4: 1,
            2: 0.5,
            1: 0,
            0.5: -0.5,
            0.25: -1,
            0: -float("inf"),
        }
        score = sum(multiplier_dict[m] for m in score)

        return score