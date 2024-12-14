def create_game_state():
    game_state_data = {
        "turn": 0,
        "player": {
            "active_pokemon": {
                "mon": None,
                "hp_percent": 1.0,
                #['none', 'SunnyDay', 'RainDance', 'Snow', 'Sandstorm' ]
                "status": [1, 0, 0, 0, 0, 0],
                "terratype": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            },
            "boosts": {
                "atk": 0.0, 
                "def": 0.0, 
                "spa": 0.0, 
                "spd": 0.0, 
                "spe": 0.0, 
                "evasion": 0.0, 
                "accuracy": 0.0
            },
            "player_side_effects": {
                "Stealth": 0, 
                "Spikes": 0, 
                "Toxic": 0, 
                "sticky_web": 0,
                "Reflect": 0, 
                "reflect_turns": 0, 
                "Tailwind": 0, 
                "tailwind_turns": 0
            },
            "last_move": None,
            "next_move": None,
            "num_mons_left": 6,
            "seen_pokemon": {
                "poke1": {"mon": "dontknow", "hp_percent": 1.0, "status": [1, 0, 0, 0, 0, 0, 0], "terratype": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]},
                "poke2": {"mon": "dontknow", "hp_percent": 1.0, "status": [1, 0, 0, 0, 0, 0, 0], "terratype": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]},
                "poke3": {"mon": "dontknow", "hp_percent": 1.0, "status": [1, 0, 0, 0, 0, 0, 0], "terratype": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]},
                "poke4": {"mon": "dontknow", "hp_percent": 1.0, "status": [1, 0, 0, 0, 0, 0, 0], "terratype": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]},
                "poke5": {"mon": "dontknow", "hp_percent": 1.0, "status": [1, 0, 0, 0, 0, 0, 0], "terratype": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]},
                "poke6": {"mon": "dontknow", "hp_percent": 1.0, "status": [1, 0, 0, 0, 0, 0, 0], "terratype": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
                     
            },
            "terra_used": 0
        },
        "opponent": {
            "active_pokemon": {
                "mon": None,
                "hp_percent": 1.0,
                #['none', 'SunnyDay', 'RainDance', 'Snow', 'Sandstorm' ]
                # ["None", "brn", "psn", "par", "slp", "frz", "tox"]
                "status": [1, 0, 0, 0, 0, 0, 0],
                "terratype": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            },
            "boosts": {
                "atk": 0.0, "def": 0.0, "spa": 0.0, "spd": 0.0, "spe": 0.0, "evasion": 0.0, "accuracy": 0.0
            },
            "opponent_side_effects": {
                "Stealth": 0, 
                "Spikes": 0, 
                "Toxic": 0, 
                "Sticky": 0,
                "Reflect": 0, 
                "reflect_turns": 0, 
                "Tailwind": 0, 
                "tailwind_turns": 0
            },
            "last_move": None,
            "next_move": None,
            "num_mons_left": 6,
            "seen_pokemon": {
                "poke1": {"mon": "dontknow", "hp_percent": 1.0, "status": [1, 0, 0, 0, 0, 0, 0], "terratype": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]},
                "poke2": {"mon": "dontknow", "hp_percent": 1.0, "status": [1, 0, 0, 0, 0, 0, 0], "terratype": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]},
                "poke3": {"mon": "dontknow", "hp_percent": 1.0, "status": [1, 0, 0, 0, 0, 0, 0], "terratype": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]},
                "poke4": {"mon": "dontknow", "hp_percent": 1.0, "status": [1, 0, 0, 0, 0, 0, 0], "terratype": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]},
                "poke5": {"mon": "dontknow", "hp_percent": 1.0, "status": [1, 0, 0, 0, 0, 0, 0], "terratype": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]},
                "poke6": {"mon": "dontknow", "hp_percent": 1.0, "status": [1, 0, 0, 0, 0, 0, 0], "terratype": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
            },
            "terra_used": 0
        },
        "battle_state": {
            #['none', 'SunnyDay', 'RainDance', 'Snow', 'Sandstorm' ]
            "weather": [1, 0, 0, 0, 0],
            "weather_turns_left": 0,
            # ['NoTerrain', 'Misty', 'Grassy', 'Electric', 'Psychic']
            "terrain": [1, 0, 0, 0, 0],
            "terrain_turns_left": 0,
            "trick_room": 0,
            "trick_room_turns": 0
        },
        "est_winrate": 0.5
    }
    return game_state_data
