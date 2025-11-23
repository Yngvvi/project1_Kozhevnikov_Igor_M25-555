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
