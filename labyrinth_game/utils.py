from labyrinth_game.constants import ROOMS
import math

# Функция описания комнаты
def describe_current_room(game_state):
    current_room = game_state['current_room']
    print(f'== {current_room.upper()} ==')
    print(ROOMS[current_room]['description'])
    if ROOMS[current_room]['items']:
        print(f"Заметные предметы: {', '.join(ROOMS[current_room]['items'])}")

    print(f"""Выходы: {', '.join([
        f'{direction} - {room}'
        for direction, room in ROOMS[current_room]['exits'].items()])}""")

    if ROOMS[current_room]['puzzle'] is not None:
        print("Кажется, здесь есть загадка (используйте команду solve).")

# Функция помощи
def show_help():
    print("\nДоступные команды:")
    print("  go <direction>  - перейти в направлении (north/south/east/west)")
    print("  look            - осмотреть текущую комнату")
    print("  take <item>     - поднять предмет")
    print("  use <item>      - использовать предмет из инвентаря")
    print("  inventory       - показать инвентарь")
    print("  solve           - попытаться решить загадку в комнате")
    print("  quit            - выйти из игры")
    print("  help            - показать это сообщение")

def pseudo_random(seed, modulo):
    if modulo <= 0:
        return 0
    x = math.sin(seed*16.4657)*45395.2463
    x = abs(x - math.floor(x))
    return int(x*modulo)

def trigger_trap(game_state):
    print("Ловушка активирована! Пол стал дрожать...")
    inventory = game_state['player_inventory']
    seed = game_state['steps_taken']
    if inventory:
        index = pseudo_random(seed, len(inventory))
        lost_item = inventory[index]
        inventory.pop(index)
        print(f'Вы теряете {lost_item}!')
    else:
        chance_damage = pseudo_random(seed, 10)
        if chance_damage < 3:
            game_state['game_over'] = True
            print('Вы попали в ловушку и проиграли.')
        else:
            print('Вам удалось увернуться! Вы уцелели.')

def random_event(game_state):
    events = ['find', 'fright', 'trap']
    seed = game_state['steps_taken']
    inventory = game_state['player_inventory']
    current_room = game_state['current_room']
    chance_event = pseudo_random(seed, 10)
    if chance_event == 0:
        event = events[pseudo_random(seed, len(events))]
        match event:
            case 'find':
                print('Вы нашли монетку!')
                inventory.append('coin')
            case 'fright':
                print('Вы слышите шорох.')
                if 'sword' in inventory:
                    print('Вы отпугнули существо мечом!')
            case 'trap':
                if current_room == 'trap_room' and 'torch' not in inventory:
                    print('В темноте вы не заметили ловушку!')
                    trigger_trap(game_state)


game_state_1 = {
        'player_inventory': ['fish', ],  # Инвентарь игрока
        'current_room': 'trap_room',  # Текущая комната
        'game_over': False,  # Значения окончания игры
        'steps_taken': 42  # Количество шагов
    }

random_event(game_state_1)