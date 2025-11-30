#!/usr/bin/env python3
from labyrinth_game.player_actions import *

def process_command(game_state, command):
    current_room = game_state['current_room']
    parts = command.split()
    if not parts:
        return
    comm = parts[0]
    param = parts[1] if len(parts) > 1 else None
    match comm:
        case 'go':
            if param:
                move_player(game_state, param)
            else:
                print("Укажите направление: go north/south/east/west")
        case 'help':
            show_help()
        case 'inventory':
            show_inventory(game_state)
        case 'look':
            describe_current_room(game_state)
        case 'quit' | 'exit':
            game_state['game_over'] = True
        case 'solve':
            if current_room == 'treasure_room':
                attempt_open_treasure(game_state)
            else:
                solve_puzzle(game_state)
        case 'take':
            if param:
                if ((current_room == 'treasure_room') and
                        (param == 'treasure_chest')):
                    print("Вы не можете поднять сундук, он слишком тяжелый.")
                else:
                    take_item(game_state, param)
            else:
                print("Укажите предмет, который нужно взять")
        case 'use':
            if param:
                use_item(game_state, param)
            else:
                print("Укажите предмет, который хотите использовать.")
        case _:
            print("Неизвестная команда. Введите 'help' для справки.")

def main():
    game_state = {
        'player_inventory': [],  # Инвентарь игрока
        'current_room': 'entrance',  # Текущая комната
        'game_over': False,  # Значения окончания игры
        'steps_taken': 0  # Количество шагов
    }

    print("Добро пожаловать в Лабиринт сокровищ!")
    describe_current_room(game_state)

    while not game_state['game_over']:
        process_command(game_state, get_input())

if __name__ == "__main__":
    main()