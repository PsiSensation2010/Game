# клетки
table_size = 3
# поле игры
table = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def draw_table():
    print(' ' * 56 + '━' * 4 * table_size)
    for i in range(table_size):
        print(' ' * 54, '┃', table[i * 3], '┃', table[1 + i * 3], '┃', table[2 + i * 3], '┃')
        print(' ' * 56 + '━' * 4 * table_size)
    pass


def game_step(index, char):
    if ((index > 9) or (index < 1)  or (table[index - 1] in ('X', 'O'))):
        return False

    table[index - 1] = char
    return True


def win():
    win = False
    win_conditionn = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))

    for position in win_conditionn:
        if (table[position[0]] == table[position[1]] and table[position[1]] == table[position[2]]):
            win = table[position[0]]


    return win


def start():
    player_1 = 'X'
    step = 1
    draw_table()


    while (step < 10) and (win() == False):

        index = input(' ' * 44 + 'Ход игрока 👉 ' + player_1 + '  Ввод номера поля  ↙ ' + '\n' + ' ' * 50 +'Для выхода нажмите "0" :')
        if index == '0':
            break
        try:
            index = int(index)
            if game_step(index, player_1):
                print('\n', '\n', ' ' * 50 + 'Отлично, продолжаем 🏄')

                if (player_1 == 'X'):
                    player_1 = 'O'
                else:
                    player_1 = 'X'

                draw_table()
                step += 1
            else:
                print(' ' * 54 + '! Неверный ход !')
        except ValueError:
            print(' '* 29 +'❗ВНИМАНИЕ для ввода принимается только одна цифра от 1-го до 9-ти ❗')

        if (step == 10 and not win()):
            print(' ' * 49 + 'Ничья, победила дружба 🤝')
        elif win() != False:
            print(' ' * 45 + '! Победа !  😎  выиграл  👉   ' + win())


print((' ' * 51 + "🙌 Крестики-нолики 🙌"))
start()
