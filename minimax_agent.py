import asyncio
import util
import json

from poke_env.player.player import Player
from poke_env.environment.abstract_battle import AbstractBattle
from poke_env.environment.move_category import MoveCategory
from poke_env.environment.pokemon import Pokemon
from poke_env.player.battle_order import BattleOrder
from poke_env.ps_client.ps_client import PSClient
from poke_env.environment.move import Move
from copy import deepcopy

class MinimaxPlayer(Player):
    def __init__(self, depth=1, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.depth = depth

    def choose_move(self, battle: AbstractBattle) -> BattleOrder:
        if not (battle.available_switches and battle.available_moves):
            return self.choose_random_move(battle)
        
        best_move, _ = self.minimax(battle, self.depth, whos_turn=True)
        return self.create_order(best_move)

    def minimax(self, battle: AbstractBattle, depth: int, whos_turn: bool):
        if depth == 0 or battle.finished:
            return None, self.eval_state(battle)
        
        if whos_turn:
            max_eval = -float("inf")
            best_move = None
            for move in self.available_actions(battle):
                # next_battle = self.simulate_turn(battle, move, whos_turn=True)
                _, curr_eval = self.minimax(battle, depth - 1, False)
                if curr_eval > max_eval:
                    max_eval = curr_eval
                    best_move = move
            return best_move, max_eval
        else:
            min_eval = float("inf")
            best_move = None
            for move in self.available_actions(battle):
                # next_battle = self.simulate_turn(battle, move, whos_turn=False)
                _, curr_eval = self.minimax(battle, depth - 1, True)
                if curr_eval < max_eval:
                    min_eval = curr_eval
                    best_move = move
            return best_move, min_eval
    
    def eval_state(self, battle: AbstractBattle) -> float:
        curr_mon = battle.active_pokemon
        opp_mon = battle.opponent_active_pokemon

        if not curr_mon or not opp_mon:
            return 0
        
        moves_with_damage = [
                (move, util.calc_damage(curr_mon, opp_mon, move)) 
                for move in battle.available_moves if isinstance(move, Move)]

        best_move, my_damage = max(moves_with_damage, key=lambda x: x[1])

        #type_score = self.type_matchup(curr_mon, opp_mon)

        hp_diff = curr_mon.current_hp_fraction - opp_mon.current_hp_fraction

        return my_damage + hp_diff * 100
    
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
    
    def simulate_turn(self, battle: AbstractBattle, move, whos_turn: bool) -> AbstractBattle:
        # battle_copy = deepcopy(battle)

        # curr_mon = battle_copy.active_pokemon if whos_turn else battle_copy.opponent_active_pokemon
        # opp_mon = battle_copy.opponent_active_pokemon if whos_turn else battle_copy.active_pokemon
        
        # if move in battle_copy.available_moves:
        #     dmg = util.calc_damage(curr_mon, opp_mon, move)
        #     opp_mon.current_hp = max(0, opp_mon.current_hp - dmg)
        # elif move in battle_copy.available_switches:
        #     battle_copy._switch
        
        # return battle_copy
        battle_dict = 1
        freeze = json.dumps(battle_dict)
        
    
    def available_actions(self, battle: AbstractBattle):
        actions = battle.available_moves or []
        actions += battle.available_switches or []
        return actions