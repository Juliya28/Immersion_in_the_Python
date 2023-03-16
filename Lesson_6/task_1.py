""" 1. Добавьте в модуль с загадками функцию, которая хранит словарь списков.
Ключ словаря - загадка, значение - список с отгадками. Функция в цикле
вызывает загадывающую функцию, чтобы передать ей все свои загадки.
"""

__all__ = [
    'atheneum',
]

_results = {}

def guess(question: str, answer: list[str], count: int) -> int:
    count_ = 0
    print(question)

    while True:
        count_ += 1
        choice = input('Введите отгадку: ').lower()

        if choice in answer:
            return count_
        if count == count_:
            return 0
        

def atheneum(count: int) -> None:
    data = {
        '--Сидит дед во сто шуб одет, кто его раздевает, тот слезы проливает--': ['лук', 'Лук', 'лучок'],
        '--И зимой и летом одним цветом--': ['елка', 'ель', 'ёлка'],
        '--Красна девица сидит в темнице, а коса на улице--': ['Морковь', 'морковь', 'морковка']
    }

    for key, item in data.items():
        add_results(key, guess(key, item, count))

    get_results(_results)



def add_results(text: str, count: int) -> None:
    _results[text] = count



def get_results(results: dict) -> None:
    print(*[f'Загадка:  "{question}" - {f"отгадана с {count} попытки" if count else f"не отгадана"}'
            for question, count in results.items()], sep='\n')



if __name__ == '__main__':
    atheneum(3)