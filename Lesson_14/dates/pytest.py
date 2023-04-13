import pytest

from .check_date import check_date, _is_leap_year


def test_is_leap():
    assert _is_leap_year(2008) == True
    assert _is_leap_year(2000) == True


def test_not_leap():
    assert _is_leap_year(2001) == False
    assert _is_leap_year(1900) == False


def test_checker():
    assert check_date('24.02.2023') == True
    assert check_date('29.02.2023') == False
    assert check_date('29.02.2020') == True
    assert check_date('29.02.1900') == False


if __name__ == '__main__':
    pytest.main(['-vv'])