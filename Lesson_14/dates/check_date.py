from sys import argv

"""
✔ Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
✔ Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
✔ Для простоты договоримся, что год может быть в диапазоне [1, 9999].
✔ Весь период (1 января 1 года — 31 декабря 9999 года) действует Григорианский календарь.
✔ Проверку года на високосность вынести в отдельную защищённую функцию.
"""

__all__ = [
    'check_date',
    '_is_leap_year',
]

_SMALL_YEAR = 4
_MIDDLE_YEAR = 100
_BIG_YEAR = 400
_FEBRUARY = 2
_LEAP_DAYS = 29
_FIRST = 1
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
    # True если кратно 400 или не кратно 100 и при этом кратно 4
    return not year % _BIG_YEAR or year % _MIDDLE_YEAR != 0 and not year % _SMALL_YEAR


def check_date(date: str) -> bool:
    day, month, year = [int(el) for el in date.split('.')]

    if _is_leap_year(year):
        spam = _DAYS.copy()
        spam[_FEBRUARY] = _LEAP_DAYS
    else:
        spam = _DAYS

    if month in spam and _FIRST <= day <= spam.get(month):
        return True
    return False


if __name__ == '__main__':
    print(check_date('24.02.2023'))
    print(check_date('29.02.2023'))
    print(check_date('29.02.2020'))
    print(check_date('01.01.0001'))
