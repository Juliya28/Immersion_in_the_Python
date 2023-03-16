""" 2. Создайте модуль и напишите в нём функцию, которая получает на вход 
дату в формате DD.MM.YYYY Функция возвращает истину, если дата может существовать 
или ложь, если такая дата невозможна.
Для простоты договоримся, что год может быть в диапазоне [1, 9999]. 
Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
Проверку года на високосность вынести в отдельную защищённую функцию.
"""

from sys import argv

__all__ = [
    'task_2'
]

_SMALL_YEAR = 4
_MIDDLE_YEAR = 100
_BIG_YEAR = 400
_FEBRUARY = 2
_LEAP_DAYS = 29
_BEGIN = 1
_DAYS = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}


def _is_leap_year(year: int) -> bool:
       return not year % _BIG_YEAR or year % _MIDDLE_YEAR != 0 and not year % _SMALL_YEAR


def task_2(date: str) -> bool:
    day, month, year = [int(el) for el in date.split('.')]

    if _is_leap_year(year):
        spam = _DAYS.copy()
        spam[_FEBRUARY] = _LEAP_DAYS
    else:
        spam = _DAYS

    if month in spam and _BEGIN <= day <= spam.get(month):
        return True
    return False


if __name__ == '__main__':
    print(task_2('24.12.2022'))
    print(task_2('29.02.2023'))
    print(task_2('29.02.2020'))
    print(task_2('01.01.1989'))
