from labyrinth_game.utils import *
# Функция отображения инвентаря
def show_inventory(game_state):
    inventory = game_state['player_inventory']
    if inventory:
        print(f"Инвентарь: {', '.join(inventory)}")
    else:
        print('Инвентарь пуст')

#Ввод пользователя
def get_input(prompt="> "):
    try:
        return input(prompt).strip()
    except (KeyboardInterrupt, EOFError):
        print("\nВыход из игры.")
        return "quit"

# Функция перемещения
def move_player(game_state, direction):
    possible_direction = ROOMS[game_state['current_room']]['exits']
    if direction in possible_direction:
        game_state['current_room'] = possible_direction[direction]
        game_state['steps_taken'] += 1
        describe_current_room(game_state)
    else:
        print("Нельзя пойти в этом направлении.")

# Функция взятия предмета
def take_item(game_state, item_name):
    current_room = game_state['current_room']
    room_items = ROOMS[current_room]['items']
    if item_name in room_items:
        game_state['player_inventory'].append(item_name)
        ROOMS[current_room]['items'].remove(item_name)
        print(f"Вы подняли:{item_name}")
    else:
        print("Такого предмета здесь нет.")

# Функция использования предмета
def use_item(game_state, item_name):
    if item_name in game_state['player_inventory']:
        match item_name:
            case 'torch':
                print('Вы зажигаете факел. Вокруг стало светлее.')
            case 'sword':
                print('Вы достаёте меч и чувствуете себя более уверенно.')
            case 'bronze_box':
                if 'rusty_key' not in game_state['player_inventory']:
                    game_state['player_inventory'].append('rusty_key')
                    print("Ржавый ключ добавлен в ваш инвентарь!")
                else:
                    print("В инвентаре уже есть ржавый ключ.")
            case _:
                print(f'Вы не знаете, как использовать {item_name}.')

    else:
        print('У вас нет такого предмета.')