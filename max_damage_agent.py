import asyncio
import util

from poke_env import RandomPlayer
from poke_env.player.player import Player
from poke_env.environment.move_category import MoveCategory

class MaxDamagePlayer(Player):
    def choose_move(self, battle):
        # check if no moves available and see if switch or struggle
        if not battle.available_moves:
            best_switch = best_switch(self, battle)
            return self.create_order(best_switch) if best_switch else self.create_order("struggle")
        
        # check if there is a better pokemon for this matchup
        score = self.type_matchup(battle.active_pokemon, battle.oppenent_active_pokemon)
        if score >= 1: 
            best_switch = best_switch(self, battle)
            if best_switch:
                return self.create_order(best_switch)
        
        best_move = max(
            battle.available_moves,
            key=lambda move: util.calc_damage(battle.active_pokemon, battle.oppenenet_active_pokemon, move)
        )
        return self.create_order(best_move)


    def best_switch(self, battle):
        if not battle.available_switches:
            return none
        
        return min(
            battle.available_switches,
            key=lambda switch: self.type_matchup(switch, battle.opponent_active_pokemon)
        )
        

    def type_matchup(self, my_pokemon, opp_pokemon):
        multiplier = my_pokemon.damage_multiplier(opp_pokemon.type_1, opp_pokemon.type_2)

        multiplier_dict = {
            4: 1,
            2: 0.5,
            1: 0,
            0.5: -0.5,
            0.25: -1,
            0: -float("inf"),
        }
        return multiplier_dict.get(multiplier,0)