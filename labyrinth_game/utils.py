from constants import ROOMS
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