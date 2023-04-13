import unittest
from .check_date import check_date, _is_leap_year


class TestDate(unittest.TestCase):
    def test_is_leap(self):
        self.assertTrue(_is_leap_year(2008))
        self.assertTrue(_is_leap_year(2000))

    def test_not_leap(self):
        self.assertFalse(_is_leap_year(1900))
        self.assertFalse(_is_leap_year(2001))

    def test_checker(self):
        self.assertTrue(check_date('24.02.2023'))
        self.assertTrue(check_date('29.02.2020'))
        self.assertFalse(check_date('29.02.2023'))
        self.assertFalse(check_date('29.02.1900'))


if __name__ == '__main__':
    unittest.main(verbosity=2)