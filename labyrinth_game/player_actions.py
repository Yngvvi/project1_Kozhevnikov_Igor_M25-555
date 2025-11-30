from labyrinth_game.utils import *
import random

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

# Функция решения загадок
def solve_puzzle(game_state):
    rewards = ['gold_coin', 'magic_dust', 'crystal', 'potion']
    current_room = game_state['current_room']
    puzzle = ROOMS[current_room]['puzzle']
    if puzzle:
        question, correct_answer = puzzle
        print(question)
        user_answer = get_input("Ваш ответ: ")
        if user_answer.lower() == correct_answer.lower():
            print('Правильно!')
            ROOMS[current_room]['puzzle'] = None
            reward = random.choice(rewards)
            game_state['player_inventory'].append(reward)
            print(f"Вы получили: {reward}!")
        else:
            print("Неверно. Попробуйте снова.")
    else:
        print('Загадок здесь нет.')

# Открытие сундука
def attempt_open_treasure(game_state):
    current_room = game_state['current_room']
    question, correct_answer = ROOMS[current_room]['puzzle']
    win_flag = False

    if 'treasure_key' in game_state['player_inventory']:
        win_flag = True
    else:
        answer = get_input(f"Сундук заперт. (подсказка:"
                           f"{question.split('подсказка:')[1]} "
                           f"Ввести код? (да/нет)")
        if answer.lower() == 'да':
            code = get_input('Введите код: ')
            if code == correct_answer:
                win_flag = True
            else:
                print('Неверный код!')
        else:
            print("Вы отступаете от сундука.")

    if win_flag:
        print("Вы применяете ключ, и замок щёлкает. Сундук открыт!")
        ROOMS[current_room]['items'].remove('treasure_chest')
        print("В сундуке сокровище! Вы победили!")
        game_state['game_over'] = True