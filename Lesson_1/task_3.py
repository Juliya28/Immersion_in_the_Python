# Задание №8
# Нарисовать в консоли ёлку спросив у пользователя количество рядов.

SPACE = ' '
STAR = '*'

rows = int(input("Сколько рядов будет у ёлки?  "))
spaces = rows-1
stars = 2

for i in range(rows):
    print(
        (SPACE*spaces) +
        (STAR*stars) +
        (SPACE*spaces)
    )
    stars += 2
    spaces -= 1

