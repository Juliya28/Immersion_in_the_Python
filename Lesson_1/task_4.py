

# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на
# школьной тетрадке.

print('                                        Таблица умножения', end='\n')
print()
 
for i in range(1, 10):
    for k in range(2, 10):
        print(f'{i} * {k} = {i * k}\t', end='')
    print('')
