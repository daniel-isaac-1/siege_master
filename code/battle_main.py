# battle_main.py
from castle_build import build_castle
from unit_selection import select_units
from battle import start_battle

def start_battle_process():
    print("\n--- Battle Setup ---")
    build_castle()
    player_units = select_units()
    start_battle(player_units)

