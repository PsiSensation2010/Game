#клетки
table_size = 3

# поле игры
table = [1, 2, 3, 4, 5, 6, 7, 8, 9]

step = 0

#игрок
player = 'X'
while step < 9:
    print((' ' * 51 + "🙌 Крестики-нолики 🙌"))
    print(' ' * 56 + '━' * 4 * table_size)
    for i in range(3):
        print(' ' * 54, '┃', table[i * 3], '┃', table[1 + i * 3], '┃', table[2 + i * 3], '┃')
        print(' ' * 56 + '━' * 4 * table_size)
    n = input(' ' * 53 + 'Куда ходим игрок ❓:')
    n = int(n)
    n -= 1
    table[n] = player
    if player == 'X':
        player = 'O'
    else:
        player = 'X'
    step += 1

print((' ' * 51 + "🙌 Крестики-нолики 🙌"))