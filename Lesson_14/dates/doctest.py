from sys import argv


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
    """
    >>> _is_leap_year(2008)
    True
    >>> _is_leap_year(2000)
    True
    >>> _is_leap_year(1900)
    False
    >>> _is_leap_year(2001)
    False
    """
    # True если кратно 400 или не кратно 100 и при этом кратно 4
    return not year % _BIG_YEAR or year % _MIDDLE_YEAR != 0 and not year % _SMALL_YEAR


def check_date(date: str) -> bool:
    """
    >>> check_date('24.02.2023')
    True
    >>> check_date('29.02.2020')
    True
    >>> check_date('29.02.2023')
    False
    >>> check_date('29.02.1900')
    False
    """
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
    import doctest
    doctest.testmod(verbose=True)
