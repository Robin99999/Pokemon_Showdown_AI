from poke_env.environment.move_category import MoveCategory
# from poke_env.data import GenData, to_id_str
from poke_env.player.player import Player
from poke_env.environment.pokemon import Pokemon

def calc_damage(my_pokemon:Pokemon, opponent_pokemon:Pokemon, move):
    type_multiplier = opponent_pokemon.damage_multiplier(move)

    # print(type_multiplier)
    # print(move)
    # print(opponent_pokemon)
    my_poke_stats = my_pokemon.stats
    opp_stats = opponent_pokemon.base_stats
    move_cat = move.category
    # print(opp_stats)
    if move_cat == MoveCategory.PHYSICAL: 
        base_damage = ((((2*my_pokemon.level)/5 + 2) * move.base_power * my_poke_stats["atk"]/opp_stats["def"])/50) + 2
    elif move_cat == MoveCategory.SPECIAL: 
        base_damage = ((((2*my_pokemon.level)/5 + 2) * move.base_power * my_poke_stats["spa"]/opp_stats["spd"])/50) + 2
    else:
        base_damage = 0
    STAB = 1.5 if move.type in my_pokemon.types else 1
    damage = base_damage * type_multiplier * move.accuracy * STAB

    return damage
