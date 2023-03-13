"""Создайте функцию генератор чисел Фибоначчи 
"""

def gen_fibonacci(qty: int) -> iter:
    first, second = 0, 1

    for num in range(qty + 1):
        yield first
        first, second = second, first + second

print(f'{gen_fibonacci(22)}\n')
print(*gen_fibonacci(22))